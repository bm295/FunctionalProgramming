def f(arr:List[Int]):List[Int] = {
    var builder = List.newBuilder[Int];
    for (i <- 0 until arr.length) {
        if (i % 2 == 1) {
            builder += arr(i);
        }
    }
    return builder.result();
}
