def f(num:Int,arr:List[Int]):List[Int] = {
    val builder = List.newBuilder[Int];
    var i = 0;
    for( i <- 1 to arr.length) {
        var j = 0;
        for (j <- 1 to num) {
            builder += i;
        }
    }
    val result = builder.result();
    return result;
}
