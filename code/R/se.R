se <- function(x)
{
    out <- sd(x)/sqrt(length(x))
    return(out)
}

v <- c(1,3,5,6,2)
print(round(se(x = v),3))