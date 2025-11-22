
block_400B23_to_400C30.bin:     file format binary


Disassembly of section .data:

0000000000400b23 <.data>:
  400b23:	0f b7 95 2e ff ff ff 	movzx  edx,WORD PTR [rbp-0xd2]
  400b2a:	0f b7 85 2c ff ff ff 	movzx  eax,WORD PTR [rbp-0xd4]
  400b31:	8d 0c 02             	lea    ecx,[rdx+rax*1]
  400b34:	0f b7 95 2a ff ff ff 	movzx  edx,WORD PTR [rbp-0xd6]
  400b3b:	0f b7 85 28 ff ff ff 	movzx  eax,WORD PTR [rbp-0xd8]
  400b42:	8d 04 02             	lea    eax,[rdx+rax*1]
  400b45:	01 c0                	add    eax,eax
  400b47:	39 c1                	cmp    ecx,eax
  400b49:	75 4a                	jne    0x400b95
  400b4b:	0f b7 85 2c ff ff ff 	movzx  eax,WORD PTR [rbp-0xd4]
  400b52:	66 3b 85 2a ff ff ff 	cmp    ax,WORD PTR [rbp-0xd6]
  400b59:	76 3a                	jbe    0x400b95
  400b5b:	0f b7 95 2e ff ff ff 	movzx  edx,WORD PTR [rbp-0xd2]
  400b62:	0f b7 85 28 ff ff ff 	movzx  eax,WORD PTR [rbp-0xd8]
  400b69:	8d 04 02             	lea    eax,[rdx+rax*1]
  400b6c:	83 e0 01             	and    eax,0x1
  400b6f:	84 c0                	test   al,al
  400b71:	75 22                	jne    0x400b95
  400b73:	66 83 bd 2e ff ff ff 	cmp    WORD PTR [rbp-0xd2],0x5
  400b7a:	05 
  400b7b:	76 18                	jbe    0x400b95
  400b7d:	66 83 bd 2e ff ff ff 	cmp    WORD PTR [rbp-0xd2],0x18
  400b84:	18 
  400b85:	77 0e                	ja     0x400b95
  400b87:	0f b7 85 28 ff ff ff 	movzx  eax,WORD PTR [rbp-0xd8]
  400b8e:	83 e0 01             	and    eax,0x1
  400b91:	85 c0                	test   eax,eax
  400b93:	75 3f                	jne    0x400bd4
  400b95:	c7 85 1c ff ff ff 00 	mov    DWORD PTR [rbp-0xe4],0x0
  400b9c:	00 00 00 
  400b9f:	eb 20                	jmp    0x400bc1
  400ba1:	8b 85 1c ff ff ff    	mov    eax,DWORD PTR [rbp-0xe4]
  400ba7:	48 98                	cdqe
  400ba9:	0f b6 44 05 90       	movzx  eax,BYTE PTR [rbp+rax*1-0x70]
  400bae:	0f be c0             	movsx  eax,al
  400bb1:	34 e9                	xor    al,0xe9
  400bb3:	89 c7                	mov    edi,eax
  400bb5:	e8 ae fa ff ff       	call   0x400668
  400bba:	83 85 1c ff ff ff 01 	add    DWORD PTR [rbp-0xe4],0x1
  400bc1:	83 bd 1c ff ff ff 31 	cmp    DWORD PTR [rbp-0xe4],0x31
  400bc8:	7e d7                	jle    0x400ba1
  400bca:	bf 01 00 00 00       	mov    edi,0x1
  400bcf:	e8 84 fa ff ff       	call   0x400658
  400bd4:	c7 85 18 ff ff ff 00 	mov    DWORD PTR [rbp-0xe8],0x0
  400bdb:	00 00 00 
  400bde:	eb 23                	jmp    0x400c03
  400be0:	8b 85 18 ff ff ff    	mov    eax,DWORD PTR [rbp-0xe8]
  400be6:	48 98                	cdqe
  400be8:	0f b6 84 05 30 ff ff 	movzx  eax,BYTE PTR [rbp+rax*1-0xd0]
  400bef:	ff 
  400bf0:	0f be c0             	movsx  eax,al
  400bf3:	34 f9                	xor    al,0xf9
  400bf5:	89 c7                	mov    edi,eax
  400bf7:	e8 6c fa ff ff       	call   0x400668
  400bfc:	83 85 18 ff ff ff 01 	add    DWORD PTR [rbp-0xe8],0x1
  400c03:	83 bd 18 ff ff ff 4f 	cmp    DWORD PTR [rbp-0xe8],0x4f
  400c0a:	7e d4                	jle    0x400be0
  400c0c:	b8 00 00 00 00       	mov    eax,0x0
  400c11:	48 8b 55 e8          	mov    rdx,QWORD PTR [rbp-0x18]
  400c15:	64 48 33 14 25 28 00 	xor    rdx,QWORD PTR fs:0x28
  400c1c:	00 00 
  400c1e:	74 05                	je     0x400c25
  400c20:	e8 93 fa ff ff       	call   0x4006b8
  400c25:	48 81 c4 e8 00 00 00 	add    rsp,0xe8
  400c2c:	5b                   	pop    rbx
  400c2d:	c9                   	leave
  400c2e:	c3                   	ret
  400c2f:	90                   	nop
