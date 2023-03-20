function solution(price) {
    return price >= 100000 ? price >= 300000 ? price >= 500000? Math.floor(0.8 * price) : Math.floor(0.9 * price) : Math.floor(0.95 * price) : price;
}