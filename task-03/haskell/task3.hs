main:: IO()

primelist :: Int->[Int]
primelist n=[x|x<-[1..n], (mod n x)==0]

checkPrime:: Int->Bool
checkPrime n=(primelist n)==[1,n]

genPrime:: Int->[Int]c
genPrime n= [x| x<-[1..n], checkPrime x]

main = do
    putStrLn "Enter an Integer:"
    input <- getLine
    let n= read input :: Int
    print(genPrime n)



