class Rev
{
public static void main(String args[])
{
int a=Integer.parseInt(args[0]);
int result=0;
while(a>0)
{
int b=a%10;
result=result*10 + b;
a=a/10;
}
System.out.println(result);
}
}

