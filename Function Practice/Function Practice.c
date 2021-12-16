#include <stdio.h>
#include <time.h>
#define FALSE 0
#define TRUE 1

int getRandomNum(int level);
void  showQuestion(int level, int num1, int num2);

int main(void)
{
	srand(time(NULL));
	int count = 0;
	int solved = 0;
	int unresolved = 0;
	for (int i = 1; i <= 5; i++)
	{
		int num1 = getRandomNum(i);
		int num2 = getRandomNum(i);
		showQuestion(i, num1, num2);
		int answer = 0;

		scanf_s("%d", &answer);


		if (answer == FALSE)
		{
			printf("------------------Error!------------------");
			exit();

		}

		if (answer == num1 * num2)
		{
			printf("\n\n-----------------맞췄습니다!!---------------\n\n");
			solved++;
			count++;
		}
		else if (answer == -1)
		{
			printf("프로그램을 종료합니다...");
			break;
		}

		else
		{
			printf("틀렸어요...\n\n");
			unresolved++;
			count++;
		}

	}
	printf("푼 문제는 %d 문제이며, 맞춘 문제는 %d 개, 틀린 문제는 %d 개 입니다!\n",
		count, solved, unresolved);
	return 0;
}

int getRandomNum(int level)
{
	return rand() % (level * 7) + 1;
}

void  showQuestion(int level, int num1, int num2)
{
	printf("------------------------------------------------------------------------------\n");
	printf("  %d단계 : %d x %d 의 값은 얼마입니까?   (-1을 입력하면 프로그램이 종료됩니다...)\n", level, num1, num2);
	printf("------------------------------------------------------------------------------\n\n");
}