import requests,random,string
import cloudscraper

sites=[
    {
        "name": "feiniao",
        "url": "https://feiniaoyun.tk/",
        "reg_url": "https://feiniaoyun.tk/api/v1/passport/auth/register",
        "sub": "https://feiniaoyun.tk/api/v1/client/subscribe?token={token}",
    },
    {
        "name":"ckcloud",
        "url":"https://www.ckcloud.xyz/",
        "reg_url":"https://www.ckcloud.xyz/api/v1/passport/auth/register",
        "sub":"https://www.ckcloud.xyz/api/v1/client/subscribe?token={token}"
    },
    {
        "name":"huanshen",
        "url":"https://www.zhenyevpn.xyz/",
        "reg_url":"https://www.zhenyevpn.xyz/api/v1/passport/auth/register",
        "sub":"https://www.zhenyevpn.xyz/api/v1/client/subscribe?token={token}"
    },
#     {
#         "name":"698436",
#         "url":"https://698436.xyz/",
#         "reg_url":"https://698436.xyz/api/v1/passport/auth/register",
#         "sub":"https://698436.xyz/api/v1/client/subscribe?token={token}"
#     },
#     {
#         "name": "xdmyyds",
#         "url": "https://xdmyyds.com/",
#         "reg_url": "https://xdmyyds.com/api/v1/passport/auth/register",
#         "sub": "https://xdmyyds.com/api/v1/client/subscribe?token={token}",
#     },
#     {
#         "name": "kelecloud",
#         "url": "https://sub5.kelecloud.xyz/",
#         "reg_url": "https://sub5.kelecloud.xyz/api/v1/passport/auth/register",
#         "sub": "https://sub5.kelecloud.xyz/api/v1/client/subscribe?token={token}",
#     },
#     {
#         "name": "misakayun.com",
#         "url": "https://misakayun.com/",
#         "reg_url": "https://misakayun.com/api/v1/passport/auth/register",
#         "sub": "https://misakayun.com/api/v1/client/subscribe?token={token}",
#     },
#     {
#         "name": "konan",
#         "url": "https://konan.ml/",
#         "reg_url": "https://konan.ml/api/v1/passport/auth/register",
#         "sub": "https://konan.ml/api/v1/client/subscribe?token={token}",
#     },
#     {
#         "name": "fkfirewall",
#         "url": "https://www.fkfirewall.top/",
#         "reg_url": "https://www.fkfirewall.top/api/v1/passport/auth/register",
#         "sub": "https://www.fkfirewall.top/api/v1/client/subscribe?token={token}",
#     },
#     {
#         "name": "pepsicola",
#         "url": "https://www.pepsicola.me/",
#         "reg_url": "https://www.pepsicola.me/api/v1/passport/auth/register",
#         "sub": "https://www.pepsicola.me/api/v1/client/subscribe?token={token}",
#     },
]

scraper = cloudscraper.create_scraper(
    browser={"browser": "chrome", "platform": "android", "desktop": False}, delay=10,
)

class tempsite():
    def __init__(self,site):
        self.reg_url=site["reg_url"]
        self.ref=site["url"]
        self.name=site["name"]
        self.sub=site["sub"]

    def register(self,email,password,proxy=None):
        headers= {
            "User-Agent":'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            "Referer": self.ref
        }
        data={
            "email":email,
            "password":password,
            "invite_code":None,
            "email_code":None
        }
        req=scraper.post(self.reg_url,headers=headers,data=data,timeout=5,proxies=proxy)
        return req
        
    def getSubscribe(self):
        password=''.join(random.sample(string.ascii_letters + string.digits + string.ascii_lowercase, 10))
        email=password+"@qq.com"
        req=self.register(email,password)
        token=req.json()["data"]["token"]
        subscribe=self.sub.format(token=token)
        return subscribe

    def saveconf(self):
        url=self.getSubscribe()
        for k in range(3):
            try:
                req=scraper.get(url,timeout=5)
                v2conf=req.text
                break
            except:
                v2conf=""
        with open("./sub/fuck/"+self.name,"w") as f:
                    f.write(v2conf)

def getconf():
    for v2site in sites:
        obj=tempsite(v2site)
        try:
            obj.saveconf()
        except:
            print(f"error:{v2site}")
            pass  
    
