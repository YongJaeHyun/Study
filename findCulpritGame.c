#include <stdio.h>
#include <time.h>

int main(void)
{
	srand(time(NULL));
	printf("\n���� ã�� ����!\n\n");
	int answer;// ����� �Է°�
	int culprit = rand() % 4; //���� (0~3)


	for (int i = 1; i <= 3; i++)
	{
		int suspect[4] = { 0,0,0,0 };
		int cntview = rand() % 2 + 2; //������ ������ ��
		int existcriminal = 0;
		printf(">>%d ��° �õ� : ", i);

		for (int j = 0; j < cntview; j++)
		{
			int randview = rand() % 4;
			if (suspect[randview] == 0)
			{
				suspect[randview] = 1;
				if (suspect[culprit] == 1)
				{
					existcriminal = 1;
				}
			}
			else
			{
				j--;
			}
		}

		for (int k = 0; k < 4; k++)
		{
			if (suspect[k] == 1)
			{
				printf("%d ", k + 1);
			}
		}
		printf("�� �����ڸ� �����մϴ�...\n");

		if (existcriminal == 1)
		{
			printf("������ �̾ȿ� �ִ�...!\n\n");
		}

		else
		{
			printf("�� �ȿ��� ������ ���µ� �ϴ�...\n\n");
			continue;
		}

	}
	printf(">>������ ��ȣ�� �Է����ּ���\n");
	scanf_s("%d", &answer);

	if (answer == culprit + 1)
	{
		printf("----------------�����̿���!--------------");
	}
	else
	{
		printf("----------------Ʋ�Ⱦ��...��--------------");
	}
	return 0;
}