#include <stdio.h>

int main(void)
{
	int floor;
	printf("층을 입력해주세요");
	scanf_s("%d", &floor);
	for (int i = 0; i < floor; i++)
	{
		for (int j = i; j < floor - 1; j++)
		{	
			printf(" ");
		}
		for (int k = 0; k < 2*i-1 ; k++)
		{
			printf("*");
		}
		printf("\n");
	}
}