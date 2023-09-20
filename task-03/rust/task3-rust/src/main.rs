//did not check for 0-1 exception 

use std::io;
fn main() {
    let mut n = String::new();
    io::stdin()
        .read_line(&mut n)
        .expect("failed to read input.");
    let n: i32 = n.trim().parse().expect("invalid input");
    
    let mut i = 2;
    while i<n{
        if is_prime(i){
            print!("{} ",i)   
        }
        i+=1;
    }
    print!("{}",'\n')
    
    
}

fn is_prime(n: i32) -> bool {
    let mut x = 2;
 
    while x<(n/2)+1{
        if n%x == 0{
          
            return false;
        }
        x+=1
    }
    return true;

}
//