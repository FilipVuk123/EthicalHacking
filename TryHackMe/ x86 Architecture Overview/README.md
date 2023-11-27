https://tryhackme.com/room/x8664arch

# Introduction

Malware often works by abusing the way systems are designed. Therefore, to understand how malware works, it is essential that we know the architecture of the systems they are running in. In this room, we will get a brief overview of the x86 architecture from a malware analysis point of view



# CPU architecture overview

The CPU architecture that is most widely used is derived from the Von Neumann architecture

## Control Unit:
The Control Unit gets instructions from the main memory, depicted here outside the CPU. The address to the next instruction to execute is stored in a register called the Instruction Pointer or IP. In 32-bit systems, this register is called EIP, and in 64-bit systems, it is called RIP.

## Arithmetic Logic Unit:
The arithmetic logic unit executes the instruction fetched from the Memory. The results of the executed instruction are then stored in either the Registers or the Memory.

## Registers:
The Registers are the CPU's storage. Registers are generally much smaller than the Main Memory, which is outside the CPU, and help save time in executing instructions by placing important data in direct access to the CPU.

## Memory:
The Memory, also called Main Memory or Random Access Memory (RAM), contains all the code and data for a program to run. When a user executes a program, its code and data are loaded into the Memory, from where the CPU accesses it one instruction at a time.


### Q. In which part of the Von Neumann architecture are the code and data required for a program to run stored?
memory

### Q. What part of the CPU stores small amounts of data?
registers

### Q. In which unit are arithmetic operations performed?
arithmetic logical unit


# Registers overview

Registers are the CPU's storage medium. The CPU can access data from the registers quicker than any other storage medium; however, its limited size means it has to be used effectively. For this purpose, the registers are divided into the following different types:

- Instruction Pointer
- General Purpose Registers
- Status Flag Registers
- Segment Registers
Let's go through each of these registers one by one below:

The Instruction Pointer is a register that contains the address of the next instruction to be executed by the CPU. It is also called the Program Counter. 

The General-Purpose registers in an x86 system are all 32-bit registers. As the name suggests, these are used during the general execution of instructions by the CPU. In 64-bit systems, these registers are extended as 64-bit registers. They contain the following registers: 

- EAX or RAX:
This is the Accumulator Register. Results of arithmetic operations are often stored in this register.

- EBX or RBX:
This register is also called the Base Register, which is often used to store the Base address for referencing an offset.

- ECX or RCX:
This register is also called the Counter Register and is often used in counting operations such as loops, etc.

- EDX or RDX:
This register is also called the Data Register. It is often used in multiplication/division operations.

- ESP or RSP:
This register is called the Stack Pointer. It points to the top of the stack and is used in conjunction with the Stack Segment register. 

- EBP or RBP:
This register is called the Base Pointer. It is used to access parameters passed by the stack. It is also used in conjunction with the Stack Segment register.

- ESI or RSI:
This register is called the Source Index register. It is used for string operations. It is used with the Data Segment (DS) register as an offset.

- EDI or RDI:
This register is called the Destination Index register. It is also used for string operations. 

- R8-R15:
These 64-bit general-purpose registers are not present in 32-bit systems. They were introduced in the 64-bit systems.



### Q. Which register holds the address to the next instruction that is to be executed?
instruction pointer

### Q. Which register in a 32-bit system is also called the Counter Register?
ecx

### Q. Which registers from the ones discussed above are not present in a 32-bit system?
R8-R15



# Registers - Continued

## Status Flag Registers:
When performing execution, some indication about the status of the execution is sometimes required. This is where the Status Flags come in. This is a single 32-bit register for 32-bit systems called EFLAGS, which is extended to 64-bits for 64-bit systems, and called RFLAGS in the 64-bit system.

- Zero Flag:
Denoted by ZF, the Zero Flag indicates when the result of the last executed instruction was zero. 

- Carry Flag:
Denoted by CF, the Carry Flag indicates when the last executed instruction resulted in a number too big or too small for the destination.

- Sign Flag:
The Sign Flag or SF indicates if the result of an operation is negative or the most significant bit is set to 1.

- Trap Flag:
The Trap Flag or TF indicates if the processor is in debugging mode. When the TF is set, the CPU will execute one instruction at a time for debugging purposes. This can be used by malware to identify if they are being run in a debugger.

Segment Registers:
Segment Registers are 16-bit registers that convert the flat memory space into different segments for easier addressing. There are six segment registers, as explained below:

- Code Segment: The Code Segment (CS ) register points to the Code section in the memory.

- Data Segment: The Data Segment (DS) register points to the program's data section in the memory.

- Stack Segment: The Stack Segment (SS) register points to the program's Stack in the memory.

- Extra Segments (ES, FS, and GS): These extra segment registers point to different data sections. These and the DS register divide the program's memory into four distinct data sections. 


### Q. Which flag is used by the program to identify if it is being run in a debugger?
trap flag

### Q. Which flag will be set when the most significant bit in an operation is set to 1?
sign flag

### Q. Which Segment register contains the pointer to the code section in memory?
code segment



# Memory overview

When a program is loaded into the Memory in the Windows Operating System, it sees an abstracted view of the Memory. This means that the program doesn't have access to the full Memory; instead, it only has access to its Memory. For that program, that is all the Memory it needs. For the sake of brevity, we will not go into the details of how the Operating System performs abstraction. We will look at the Memory as a program sees it, as that is more relevant to us when reverse-engineering malware.

We can find a brief overview of the four sections below.

- Code:
The Code Section, as the name implies, contains the program's code. Specifically, this section refers to the text section in a Portable Executable (PE) file, which includes instructions executed by the CPU. This section of the Memory has execute permissions, meaning that the CPU can execute the data in this section of the program memory.

- Data:
The Data section contains initialized data that is not variable and remains constant. It refers to the data section in a Portable Executable file. It often contains Global variables and other data that are not supposed to change during the program's execution.

- Heap:
The heap, also known as dynamic Memory, contains variables and data created and destroyed during program execution. When a variable is created, memory is allocated for that variable at runtime. And when that variable is deleted, the memory is freed. Hence the name dynamic memory.

- Stack:
The Stack is one of the important parts of the Memory from a malware analysis point of view. This section of the Memory contains local variables, arguments passed on to the program, and the return address of the parent process that called the program. Since the return address is related to the control flow of the CPU's instructions, the stack is often targeted by malware to hijack the control flow -> Buffer Overflows


### Q. When a program is loaded into Memory, does it have a full view of the system memory? Y or N?
n

### Q. hich section of the Memory contains the code?
code

### Q. Which Memory section contains information related to the program's control flow?
stack


# Stack Layout

The stack is a Last In First Out (LIFO) memory. This means that the last element pushed onto the stack is the first one to be popped out. For example, if we push A, B, and C onto the stack, when we pop out these elements, the first to pop out will be C, B, and then A. The CPU uses two registers to keep track of the stack. One is the Stack Pointer (the ESP or RSP), and the other is the Base Pointer (the EBP or RBP).



## The Stack Pointer:
The Stack Pointer points to the top of the stack. When any new element is pushed on the stack, the location of the Stack Pointer changes to consider the new element that was pushed on the stack. Similarly, when an element is popped off the stack, the stack pointer adjusts itself to reflect that change. 

## The Base Pointer:
The Base Pointer for any program remains constant. This is the reference address where the current program stack tracks its local variables and arguments.


