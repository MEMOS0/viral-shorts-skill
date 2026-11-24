"""Automatic archive finder: searches free, licence-tagged sources for real photos/documents
matching each line of a script, downloads them and writes a credits file.

Sources (all public APIs, no key needed): Wikimedia Commons, NASA Image Library,
Library of Congress, Openverse (CC search), Internet Archive.

usage: python find_archive.py queries.txt outdir
queries.txt: one line per shot ->  shot_id | query | optional must-word
Output: outdir/<shot_id>_<n>.<ext>, outdir/credits.csv (file, source, title, author, licence, url, page).
Accepts only PD/CC0, CC BY, CC BY-SA and "no known restrictions"; rejects ND, NC, unknown and free-text licences.
NASA media are flagged "review": NASA content is generally not copyrighted, but third-party material, logos and
identifiable people (no endorsement) need checking. Never accepts results without a licence field. Review every file by eye before use.
"""
import urllib.error,csv,json,os,re,sys,time,urllib.parse,urllib.request
UA={"User-Agent":"archive-finder/1.0 (research; contact via repo)"}
REJECT=re.compile(r"\bnd\b|no[- ]?deriv|\bnc\b|non[- ]?commercial|all rights reserved|fair use|copyrighted|editorial use|permission",re.I)
ACCEPT=[(re.compile(r"^(public domain|pdm?\b|pd-\S+|cc0|cc[- ]?zero)",re.I),"PD/CC0"),
        (re.compile(r"\bno known (copyright )?restrictions\b",re.I),"No known restrictions (verify)"),
        (re.compile(r"\bcc[- ]by[- ]sa\b",re.I),"CC BY-SA (share-alike: derivative must keep CC BY-SA)"),
        (re.compile(r"\bcc[- ]by\b(?![- ](nc|nd|sa))",re.I),"CC BY (credit required)")]
def classify_licence(lic):
    """Return a normalised licence label or None (= reject). ND, NC, unknown and free text are rejected."""
    t=re.sub(r"^cc\s+(?=(cc0|pdm)\b)","",(lic or "").strip(),flags=re.I)
    if not t or REJECT.search(t): return None
    for rx,label in ACCEPT:
        if rx.search(t): return label
    return None
def fetch(u,tries=4):
    for t in range(tries):
        try: return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
        except urllib.error.HTTPError as e:
            if e.code!=429 or t==tries-1: raise
            time.sleep(5*(t+1))
def get(u): return json.loads(fetch(u))
def commons(q,n=6):
    u="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode(dict(action="query",format="json",generator="search",
      gsrsearch=q+" filetype:bitmap",gsrnamespace=6,gsrlimit=n,prop="imageinfo",iiprop="url|extmetadata",iiurlwidth=2000))
    for p in (get(u).get("query",{}).get("pages",{}) or {}).values():
        ii=p["imageinfo"][0];m=ii.get("extmetadata",{})
        yield dict(source="Wikimedia Commons",title=p["title"],url=ii.get("thumburl") or ii["url"],page=ii.get("descriptionurl"),
          author=re.sub("<[^>]+>","",m.get("Artist",{}).get("value",""))[:120],licence=m.get("LicenseShortName",{}).get("value",""))
def nasa(q,n=6):
    for it in get("https://images-api.nasa.gov/search?"+urllib.parse.urlencode(dict(q=q,media_type="image")))["collection"]["items"][:n]:
        d=it["data"][0];href=it["links"][0]["href"] if it.get("links") else None
        if href: yield dict(source="NASA",title=d.get("title",""),url=href,page="https://images.nasa.gov/details/"+d["nasa_id"],author=d.get("center",""),licence="NASA media (usually not copyrighted; check for third-party credit, logos, identifiable people)",nasa=True)
def loc(q,n=6):
    for r in get("https://www.loc.gov/photos/?"+urllib.parse.urlencode(dict(q=q,fo="json",c=n))).get("results",[])[:n]:
        im=(r.get("image_url") or [None])[-1]
        if im: yield dict(source="Library of Congress",title=r.get("title",""),url=im,page=r.get("url"),author="",licence="; ".join(r.get("rights_advisory",[]) or ["No known copyright restrictions" if "no known" in json.dumps(r).lower() else ""]))
def openverse(q,n=6):
    for r in get("https://api.openverse.org/v1/images/?"+urllib.parse.urlencode(dict(q=q,page_size=n,license_type="commercial")))["results"]:
        yield dict(source="Openverse/"+r.get("source",""),title=r.get("title",""),url=r["url"],page=r.get("foreign_landing_url"),author=r.get("creator",""),licence=f"CC {r.get('license','')} {r.get('license_version','')}")
def internet_archive(q,n=6):
    u="https://archive.org/advancedsearch.php?"+urllib.parse.urlencode({"q":f"({q}) AND mediatype:image","fl[]":["identifier","title","creator","licenseurl"],"rows":n,"output":"json"},doseq=True)
    for r in get(u).get("response",{}).get("docs",[]):
        lu=r.get("licenseurl","") or ""
        lic="public domain" if re.search(r"publicdomain|/mark/|/zero/",lu) else ("CC BY-SA" if "/by-sa/" in lu else "CC BY" if re.search(r"/by/",lu) else "")
        if lic and re.search(r"/by-nd|/by-nc|/nd/|/nc",lu): lic=""
        ident=r["identifier"]
        yield dict(source="Internet Archive",title=str(r.get("title","")),url=f"https://archive.org/services/img/{ident}",page="https://archive.org/details/"+ident,author=str(r.get("creator",""))[:120],licence=lic)
SRC=[commons,nasa,loc,openverse,internet_archive]
def main(qf,out):
    os.makedirs(out,exist_ok=True);rows=[];seen=set()
    for line in open(qf,encoding="utf-8"):
        if "|" not in line: continue
        sid,q,*must=[x.strip() for x in line.split("|")];k=0
        for s in SRC:
            try: res=list(s(q))
            except Exception as e: print("ERR",s.__name__,q,e); continue
            for r in res:
                lab="NASA (review)" if r.pop("nasa",False) else classify_licence(r["licence"])
                if r["url"] in seen or not lab: continue
                r["licence_class"]=lab
                if must and must[0] and must[0].lower() not in (r["title"]+" "+(r["page"] or "")).lower(): continue
                ext=os.path.splitext(urllib.parse.urlparse(r["url"]).path)[1][:5] or ".jpg";fn=f"{sid}_{k}{ext}"
                try: open(os.path.join(out,fn),"wb").write(fetch(r["url"].split("?")[0])); time.sleep(1.5)
                except Exception as e: print("DLERR",r["url"],e); continue
                seen.add(r["url"]);rows.append(dict(file=fn,shot=sid,query=q,**r));k+=1
                if k>=4: break
            if k>=4: break
        print(sid,q,"->",k)
    with open(os.path.join(out,"credits.csv"),"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["file","shot","query","source","title","author","licence","licence_class","url","page"]);w.writeheader();w.writerows(rows)
if __name__=="__main__": main(*sys.argv[1:3])
