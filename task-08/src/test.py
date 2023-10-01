import requests
import PIL.Image as Image
poke="charizard"
res=requests.get("https://pokeapi.co/api/v2/pokemon/"+poke)
if res.status_code==404:
        pass
else:
    res_js=res.json()
    name=res_js["name"]
    ability1=res_js["abilities"][0]["ability"]["name"]
    ability2=res_js["abilities"][1]["ability"]["name"]
    type=res_js["types"][0]["type"]["name"]
    hp=res_js["stats"][0]["base_stat"]
    attack=res_js["stats"][1]["base_stat"]
    defense=res_js["stats"][2]["base_stat"]
    spec_attck=res_js["stats"][3]["base_stat"]
    spec_dfnc=res_js["stats"][4]["base_stat"]
    speed=res_js["stats"][5]["base_stat"]
    img_lnk=res_js["sprites"]["front_default"]

    img = Image.open(requests.get(img_lnk, stream = True).raw)
    img.save('greenland_02a.png')
    img=requests.get(img_lnk)
    '''f= open("temp.png","w") 
    f.write(img.content)
    f.flush()
    f.close()'''
    print(name,ability1, ability2,type,hp,attack,defense,spec_attck,spec_dfnc,speed , sep="\n")
    