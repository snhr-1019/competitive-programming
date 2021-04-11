fun main(){
    val (a, b) = readLine()!!.split(" ").map{ it.toInt() }
    println(Math.max(a - 2*b,0));
}
