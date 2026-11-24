import json,subprocess,os,re,sys,whisper,glob
import numpy as np
from PIL import Image
P={p["id"]:p for p in json.load(open("pick.json"))}
m=whisper.load_model("small.en"); out=json.load(open("full.json")) if os.path.exists("full.json") else []
done={o["id"] for o in out}; os.makedirs("sheets",exist_ok=True)
def dur(f): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",f],capture_output=True,text=True).stdout.strip() or 0)
for f in sorted(glob.glob("v/*.mp4")):
    i=os.path.basename(f)[:-4]
    if i in done or i not in P: continue
    p=dict(P[i]); D=dur(f)
    r=m.transcribe(f,word_timestamps=True,fp16=__import__("torch").cuda.is_available(),language="en")
    words=[(w["word"].strip(),round(w["start"],2),round(w["end"],2)) for s in r["segments"] for w in s.get("words",[])]
    sc=subprocess.run(["ffmpeg","-i",f,"-vf","select='gt(scene,0.28)',showinfo","-an","-f","null","-"],capture_output=True,text=True,errors="replace").stderr
    cuts=[round(float(x),2) for x in re.findall(r"pts_time:([\d.]+)",sc)]
    lo=subprocess.run(["ffmpeg","-i",f,"-af","ebur128=metadata=1,ametadata=print:key=lavfi.r128.M","-f","null","-"],capture_output=True,text=True,errors="replace").stderr
    M=[float(x) for x in re.findall(r"lavfi.r128.M=(-?[\d.]+)",lo)]
    persec=[round(max(M[k*10:(k+1)*10] or [-70]),1) for k in range(int(D)+1)] if M else []
    I=re.findall(r"I:\s+(-?[\d.]+) LUFS",lo)
    # 1 fps contact sheet
    subprocess.run(["ffmpeg","-y","-i",f,"-vf","fps=2,scale=135:240,tile=10x%d"%max(1,int(D*2/10)+1),"-frames:v","1",f"sheets/{i}.jpg"],capture_output=True)
    # loop similarity first vs last frame
    subprocess.run(["ffmpeg","-y","-ss","0.1","-i",f,"-frames:v","1","-vf","scale=64:114","a.png"],capture_output=True)
    subprocess.run(["ffmpeg","-y","-sseof","-0.2","-i",f,"-frames:v","1","-vf","scale=64:114","b.png"],capture_output=True)
    try: loop=round(float(np.abs(np.asarray(Image.open("a.png").convert("L"),float)-np.asarray(Image.open("b.png").convert("L"),float)).mean()),1)
    except Exception: loop=None
    sl=np.diff([0]+cuts+[D]) if D else []
    p.update(dur=round(D,1),text=r["text"].strip(),words=words,cuts=cuts,ncuts=len(cuts),
      med_shot=round(float(np.median(sl)),2) if len(sl) else None,first_cut=cuts[0] if cuts else None,
      wpm=round(len(words)/max(D,1)*60),first_word=words[0][1] if words else None,
      hook=" ".join(w[0] for w in words if w[1]<3.0),lufs=float(I[-1]) if I else None,persec=persec,loopdiff=loop)
    out.append(p); json.dump(out,open("full.json","w"),indent=1); print(i,p["dur"],p["ncuts"],p["med_shot"],p["hook"][:80],flush=True)
print("ANDONE")
