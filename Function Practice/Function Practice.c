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
			printf("\n\n-----------------������ϴ�!!---------------\n\n");
			solved++;
			count++;
		}
		else if (answer == -1)
		{
			printf("���α׷��� �����մϴ�...");
			break;
		}

		else
		{
			printf("Ʋ�Ⱦ��...\n\n");
			unresolved++;
			count++;
		}

	}
	printf("Ǭ ������ %d �����̸�, ���� ������ %d ��, Ʋ�� ������ %d �� �Դϴ�!\n",
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
	printf("  %d�ܰ� : %d x %d �� ���� ���Դϱ�?   (-1�� �Է��ϸ� ���α׷��� ����˴ϴ�...)\n", level, num1, num2);
	printf("------------------------------------------------------------------------------\n\n");
}