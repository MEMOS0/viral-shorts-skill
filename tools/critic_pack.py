"""Build an evidence pack from a RENDERED video so an independent critic model can judge it
without trusting the producer's own score.

usage: python critic_pack.py video.mp4 outdir
Produces: contact sheet (2 fps), first-3-s frames (10 fps), transcript with word times (Whisper),
cuts, freeze/black detection, loudness (integrated + per second), first/last frame diff,
and pack.md which is pasted together with references/12-critic-agent.md into a DIFFERENT model.
"""
import json,os,re,subprocess,sys
def sh(*a): return subprocess.run(a,capture_output=True,text=True,errors="replace")
def main(f,out):
    os.makedirs(out,exist_ok=True)
    D=float(sh("ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f).stdout or 0)
    sh("ffmpeg","-y","-i",f,"-vf",f"fps=2,scale=180:320,tile=10x{int(D*2/10)+1}","-frames:v","1",f"{out}/contact_2fps.jpg")
    sh("ffmpeg","-y","-t","3","-i",f,"-vf","fps=10,scale=270:480,tile=10x3","-frames:v","1",f"{out}/first3s_10fps.jpg")
    cuts=[round(float(x),2) for x in re.findall(r"pts_time:([\d.]+)",sh("ffmpeg","-i",f,"-vf","select='gt(scene,0.28)',showinfo","-an","-f","null","-").stderr)]
    fd=sh("ffmpeg","-i",f,"-vf","freezedetect=n=0.003:d=1.5,blackdetect=d=0.3","-an","-f","null","-").stderr
    freezes=re.findall(r"freeze_start: ([\d.]+)",fd); blacks=re.findall(r"black_start:([\d.]+)",fd)
    lo=sh("ffmpeg","-i",f,"-af","ebur128=peak=true","-f","null","-").stderr
    I=re.findall(r"I:\s+(-?[\d.]+) LUFS",lo); TP=re.findall(r"Peak:\s+(-?[\d.]+) dBFS",lo)
    words=[]
    try:
        import whisper; r=whisper.load_model("base.en").transcribe(f,word_timestamps=True,language="en")
        words=[(w["word"].strip(),round(w["start"],2)) for s in r["segments"] for w in s.get("words",[])]
    except Exception as e: print("whisper skipped:",e)
    shots=[round(b-a,2) for a,b in zip([0]+cuts,cuts+[D])]
    M=dict(duration=round(D,2),cuts=cuts,longest_shot=max(shots) if shots else D,freezes_over_1_5s=freezes,black_frames=blacks,
           lufs=I[-1] if I else None,true_peak=TP[-1] if TP else None,first_word=words[0][1] if words else None)
    json.dump(dict(metrics=M,words=words),open(f"{out}/metrics.json","w"),indent=1)
    line=lambda a,b:" ".join(w for w,t in words if a<=t<b)
    with open(f"{out}/pack.md","w",encoding="utf-8") as o:
        o.write("# Critic pack\n\nAttached images: contact_2fps.jpg (2 frames per second, left→right, top→bottom), first3s_10fps.jpg.\n\n")
        o.write("## Metrics\n```json\n"+json.dumps(M,indent=1)+"\n```\n\n## Transcript by second\n")
        for s in range(int(D)+1): o.write(f"- {s:>3}s  {line(s,s+1)}\n")
    print(json.dumps(M))
if __name__=="__main__": main(*sys.argv[1:3])
