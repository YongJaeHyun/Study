#include <stdio.h>

int main(void)
{
	int 철수 = 1;
	int 영희 = 2;
	int 민수 = 3;
	printf(" 철수네 주소는 : %d , 암호는 : %d 입니다.\n", &철수, 철수);
	int* 미션맨 = &철수;
	printf(" 미션맨이 방문하는 곳 주소 : %d, 암호 : %d\n", 미션맨, *미션맨);
	int* 스파이 = &철수;
	*스파이 = 철수 - 2;
	printf(" 스파이가 바꾼 암호를 바꾼 곳 주소 : %d , 암호 : %d\n", 스파이, *스파이);
	return 0;
}