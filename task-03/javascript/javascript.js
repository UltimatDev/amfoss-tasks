n=window.prompt("Enter Number U want to find Prime Numbers till:-");
let x=2;
let check=true;
while (x<=n) {
    check=true;
    for(let i=2; i<=(x/2)+1;){//as explained in the py file 
        if(x%i==0 && x!=i){//second condition is for some probems that arose for 2 and 3
            check=false;
            break
        } 
        i++;
    }
    if (check){
        console.log(x)
    }
    x++;
}