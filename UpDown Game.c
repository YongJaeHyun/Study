#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	printf("\n���� ���߱�  (1~100)\n\n");
	srand(time(NULL));
	int my=101;
	int num;
	num = rand() % 100+1;
	while (my != num)
	{
		printf("---------------------\n");
		printf(" ���ڸ� �Է����ּ���\n");
		printf("---------------------\n");
		scanf_s("%d", &my);
		if (my < num)
		{
			printf("Up\n\n");
		}
		else if (my > num)
		{
			printf("Down\n\n");
		}
		else
			break;
	}
	printf("Win\n\n\nAnswer = %d\n", num);
	return 0;
}				