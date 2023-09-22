window.onload=function(){
    document.getElementById("buttn").addEventListener("click", getWeather)
    if (window.navigator.onLine==true){
        document.getElementById("netstat").innerHTML="🟢Online"
  }
  else{
    document.getElementById("netstat").innerHTML="Offline"
  }
}


async function getWeather() {
    if (window.navigator.onLine==true){
        document.getElementById("netstat").innerHTML="Online"
        const apikey="0c44d6d837b199566e93f3dbd3f62108"
        let city_name= document.getElementById("cityname").value;
        let apiurl = `https://api.openweathermap.org/data/2.5/weather?q=${city_name}&appid=${apikey}`
        let res= await fetch(apiurl)
        rescode=res.status
        if (rescode==200){
            const data= await res.json();
            let temp=data.main.temp-273
            temp=Math.round(temp*100)/100 //logical way to round of the number to two decimal places
            document.getElementById("temp").innerHTML=rescode
            document.getElementById("desc").innerHTML=data.weather[0].main}
        else{
            document.getElementById("temp").innerHTML="Error"
        }
    }else{
        document.getElementById("netstat").innerHTML="Offline"
    }
}

