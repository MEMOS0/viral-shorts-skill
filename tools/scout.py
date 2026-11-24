# Build a top/median/bottom sample per channel from the Shorts tab, then download.
import json,subprocess,os,sys,statistics
CH=["zackdfilms","MarkRober","veritasium","NileRed","RealEngineering","kurzgesagt","MrBallen",
"PracticalEngineeringChannel","TheB1M","HistoryLegends","simplehistory","bigthink","MustardChannel",
"WendoverProductions","InterestingEngineering","ScienceNaturePage","TheInfographicsShow",
"Fern-TV","PlainlyDifficult","NEOexplains","ColdFusion","MentourPilot","AlternateHistoryHub",
"MagnatesMedia","Sideprojects","Brickhousedocs","EngineeringExplained","ScienceGoneWrong"]
YT=[sys.executable,"-m","yt_dlp","--js-runtimes","node"]
pick=[];os.makedirs("lists",exist_ok=True)
for h in CH:
    try:
        r=subprocess.run(YT+["--flat-playlist","-J","--playlist-end","160",f"https://www.youtube.com/@{h}/shorts"],capture_output=True,text=True,timeout=240)
        E=[e for e in json.loads(r.stdout).get("entries",[]) if e.get("view_count")]
    except Exception as ex: print("FAIL",h,ex,flush=True); continue
    E=E[10:] if len(E)>40 else E          # drop newest 10: views not settled yet
    if len(E)<12: print("SKIP",h,len(E),flush=True); continue
    E.sort(key=lambda e:-e["view_count"]); n=len(E); m=n//2
    sel=[("top",e) for e in E[:6]]+[("mid",e) for e in E[m-2:m+3]]+[("low",e) for e in E[-5:]]
    med=statistics.median(e["view_count"] for e in E)
    for tier,e in sel:
        pick.append(dict(ch=h,views=e["view_count"],title=e.get("title",""),id=e["id"],tier=tier,ch_median=med,ch_n=n))
    print("OK",h,n,int(med),flush=True)
json.dump(pick,open("pick2.json","w"),indent=1); print("PICKED",len(pick),flush=True)
for p in pick:
    f=f"v/{p['id']}.mp4"
    if os.path.exists(f): continue
    subprocess.run(YT+["-q","-f","bv*[height<=360]+ba/b[height<=360]/b","--merge-output-format","mp4","-o",f,"https://www.youtube.com/shorts/"+p["id"]],timeout=300)
print("DLDONE",flush=True)
