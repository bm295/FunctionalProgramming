def f(arr:List[Int]):Int = {
    var result = 0;
    for (i <- 0 until arr.length) {
        if (arr(i) % 2 != 0) {
            result += arr(i);
        }
    }
    return result;
}