#include <stdio.h>
#include <time.h>
#include <stdlib.h>


int main(void)
{
	srand(time(NULL));
	int num1 = 0;
	int num2 = 0;
	int num3 = 0;
	int num4 = 0;
	while (num1 == num2 || num1 == num3 || num1 == num4 || num2 == num3 ||
		   num2 == num4 || num3 == num4)
	{
		num1 = rand() % 9 + 1;
		num2 = rand() % 10;
		num3 = rand() % 10;
		num4 = rand() % 10;
	}
	int mynum1 = 0, mynum2 = 0 , mynum3 = 0, mynum4 = 0;

	while ((num1 != mynum1) || (num2 != mynum2) || (num3 != mynum3) || (num4 != mynum4))
	{
		int Strike = 0;
		int Ball = 0;
		printf("���ڸ� ������� ���� �ٸ��� �Է����ּ��� (0~9) --- ��, ù ��° ���� 0 ���� --- \n\n");
		scanf_s("%d%d%d%d", &mynum1, &mynum2, &mynum3, &mynum4);
		printf("\n\n%d %d %d %d", mynum1, mynum2, mynum3, mynum4);
		if ((mynum1 == mynum2) || (mynum1 == mynum3) || (mynum1 == mynum4) || (mynum2 == mynum3)||
			(mynum2 == mynum4) || (mynum3 == mynum4))
		{
			while ((mynum1 == mynum2) || (mynum1 == mynum3) || (mynum1 == mynum4) || (mynum2 == mynum3) ||
				(mynum2 == mynum4) || (mynum3 == mynum4))
			{
				printf("\n\n4���� ���ڸ� ���� �ٸ��� �Է����ּ���!\n");
				scanf_s("%d%d%d%d", &mynum1, &mynum2, &mynum3, &mynum4);
				printf("\n\n%d %d %d %d", mynum1, mynum2, mynum3, mynum4);
			}
			
		}
		if (mynum1 == 0)
		{
			while (mynum1 == 0)
			{
				printf("\n\nù ��° ���ڴ� 0�� �� �� �����ϴ�!\n");
				scanf_s("%d%d%d%d", &mynum1, &mynum2, &mynum3, &mynum4);
				printf("\n\n%d %d %d %d", mynum1, mynum2, mynum3, mynum4);
			}
		}
		if ((mynum1 == num1) && (mynum2 == num2) && (mynum3 == num3) && (mynum4 == num4))
		{
			break;
		}
	    if (mynum1 == num1) 
		{
			Strike++;
		}
		if (mynum2 == num2)
		{
			Strike++;
		}
		if (mynum3 == num3)
		{
			Strike++;
		}
	    if (mynum4 == num4)
		{
			Strike++;
		}
		if (mynum1 == num2)
		{
			Ball++;
		}
		if (mynum1 == num3)
		{
			Ball++;
		}
		if (mynum1 == num4)
		{
			Ball++;
		}
		if (mynum2 == num1)
		{
			Ball++;
		}
		if (mynum2 == num3)
		{
			Ball++;
		}
		if (mynum2 == num4)
		{
			Ball++;
		}
		if (mynum3 == num1)
		{
			Ball++;
		}
		if (mynum3 == num2)
		{
			Ball++;
		}
		if (mynum3 == num4)
		{
			Ball++;
		}
		if (mynum4 == num1)
		{
			Ball++;
		}
		if (mynum4 == num2)
		{
			Ball++;
		}
		if (mynum4 == num3)
		{
			Ball++;
		}
		
		if (Ball== 0 && Strike == 0)
		{
			printf("\n\n\n�̵����� �ƴϳ׿�... �ٽ� ����!\n");
		}
		printf("\n%dS %dB\n\n", Strike, Ball);
	}
	printf("\n\n\n\n------------<<<< �����Դϴ�!! >>>--------------");

	return 0;
}