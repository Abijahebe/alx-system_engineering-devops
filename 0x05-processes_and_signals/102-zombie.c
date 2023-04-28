#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>


/**
 * infinit_while - Run an infinite while loop.
 *
 * Return: Always 0.
 */
int infinit_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * main - Creates five zombie processes.
 *
 * Return: Always 0.
 */
int main(void)
{
	pid_t pid
		int 1;

	for (i = 0; i < 5; ++i)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
		else
			exit(0);
	}

	infinite_while();
	return (0);
}
