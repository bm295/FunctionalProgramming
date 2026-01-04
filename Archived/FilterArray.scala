def f(delim:Int,arr:List[Int]):List[Int] = {
    var builder = List.newBuilder[Int];
    for (x <- arr) {
        if (x < delim) {
            builder += x
        }
    }
    return builder.result();
}
