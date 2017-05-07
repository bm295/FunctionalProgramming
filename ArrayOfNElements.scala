def f(num:Int) : List[Int] = {
    var builder = List.newBuilder[Int];
    var i = 0;
    for(i <- 1 to num) {
        builder += i;
    }
    val list = builder.result()

    //print(list + "\n")
    return list
} 
