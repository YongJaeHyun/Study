#include <stdio.h>
#include <time.h>

int main(void)
{
	srand(time(NULL));
	printf("\n범인 찾기 게임!\n\n");
	int answer;// 사용자 입력값
	int culprit = rand() % 4; //범인 (0~3)


	for (int i = 1; i <= 3; i++)
	{
		int suspect[4] = { 0,0,0,0 };
		int cntview = rand() % 2 + 2; //조사할 피의자 수
		int existcriminal = 0;
		printf(">>%d 번째 시도 : ", i);

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
		printf("번 피의자를 조사합니다...\n");

		if (existcriminal == 1)
		{
			printf("범인은 이안에 있다...!\n\n");
		}

		else
		{
			printf("이 안에는 범인이 없는듯 하다...\n\n");
			continue;
		}

	}
	printf(">>범인의 번호를 입력해주세요\n");
	scanf_s("%d", &answer);

	if (answer == culprit + 1)
	{
		printf("----------------정답이에요!--------------");
	}
	else
	{
		printf("----------------틀렸어요...ㅜ--------------");
	}
	return 0;
}