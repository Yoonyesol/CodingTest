function solution(my_string) {
    "aeiou".split("").forEach((cur, idx)=> {
        if (my_string.includes(cur)){
            my_string = my_string.replaceAll(cur, "")
        }
    });
    return my_string;
}