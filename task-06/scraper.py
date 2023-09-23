from urllib.request import urlopen
from bs4 import BeautifulSoup as bsp
import csv
from datetime import datetime

f=open(r'score.csv','a',newline='')
w=csv.writer(f)
def getscore():
    urllink="https://www.espncricinfo.com/live-cricket-score"
    try:
        site=urlopen(urllink)
    except:
        print("no site")
        return 0
    rdst=site.read()
    site.close()


    pg_txt = bsp(rdst,'html.parser')

    match_det=pg_txt.find_all('div',class_="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-my-1")
    
    pg_sum= pg_txt.find('p', class_="ds-text-tight-s ds-font-regular ds-truncate ds-text-typo")
    
    mat_t1_score= pg_txt.find('div',class_="ds-text-compact-s ds-text-typo ds-text-right ds-whitespace-nowrap")

    #tme=datetime.date()
    #tme=pg_txt.find('div',class_="ds=text-tight-xs ds-truncate ds-text-typo-mid3")
    
    
   
 
    if match_det:
        if match_det[0].find('strong'):
            t1=match_det[0].find('p').text
        else:
            t1=""
        mat_score_1 = match_det[0].find('strong').text 
        mat_over_1 = match_det[0].find('span').text if match_det[0].find('span') else ""
        t2= match_det[1].find('p').text
        ex=pg_txt.find('div',class_="ci-team-score ds-flex ds-justify-between ds-items-center ds-text-typo ds-opacity-50 ds-my-1")
        scoret1=mat_t1_score.find('strong').text
        if ex:
            t2_temp=ex.find('p').text
            if t2_temp != t2:
                t2=""
                scoret1=""
            else:
                pass

      
            
        summ=pg_sum.find('span').text
        response=f'''
        {t1} {scoret1}

{t2}

{mat_score_1}  {mat_over_1}
{summ}
            '''
        dtetme=datetime.now()
        w.writerow([t1,scoret1,t2,mat_score_1,mat_over_1,summ,dtetme])
        f.flush()
        
       
        return response
getscore()