#include <stdio.h>
int main(void)
{
/* {
	int one, two, three;
	printf("3개의 정수를 입력해주세요 : ");
	scanf_s("%d %d %d", &one,&two, &three);
	printf("%d\n", one);
	printf("%d\n", two);
	printf("%d\n", three);
}*/
//프로젝트
	char name[256];
	printf("이름이 뭐에요?");
	scanf_s("%s", name, sizeof(name));

	int age;
	printf("몇 살이에요?");
	scanf_s("%d", &age);

	float weight;
	printf("몸무게는 몇 kg 이에요?");
	scanf_s("%f", &weight);

	double height;
	printf("키는 몇 cm이예요?");
	scanf_s("%lf", &height);

	char what[256];
	printf("무슨 범죄를 저지르셨어요?");
	scanf_s("%s", what, sizeof(what));

	printf("\n\n-- - 범죄자 정보-- - \n\n");
	printf("이름      : %s\n", name);
	printf("나이      : %d\n", age);
	printf("몸무게    : %.2f\n", weight);
	printf("키        : %.2lf\n", height);
	printf("범죄      : %s\n", what);
	return 0;
	}