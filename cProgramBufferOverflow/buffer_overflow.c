#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define password "password123"

int checkpw(){
	printf("Please enter password: ");
	char pw[100];
	gets(pw);
	if (strcmp (password, pw) == 0){
		granted();
	}else {
		printf("Wrong password\n");
	}
	return 0;
}

int granted(){
	printf("Access GRANTED!!!\n");
	return 0;
}

int main (int argc, char * argv[]){
	setuid(1000);
	if (argc > 1){
		printf("There is no usage!\n");
		exit(1);
	}

	checkpw();
	return 0;
}
