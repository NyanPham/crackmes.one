
full_block.bin:     file format binary


Disassembly of section .data:

0000000000400a62 <.data>:
  400a62:	e9 48 89 c0 c7       	jmp    0xffffffffc80093af
  400a67:	85 20                	test   DWORD PTR [rax],esp
  400a69:	ff                   	(bad)
  400a6a:	ff                   	(bad)
  400a6b:	ff 00                	inc    DWORD PTR [rax]
  400a6d:	00 00                	add    BYTE PTR [rax],al
  400a6f:	00 e9                	add    cl,ch
  400a71:	90                   	nop
  400a72:	00 00                	add    BYTE PTR [rax],al
  400a74:	00 8b 85 20 ff ff    	add    BYTE PTR [rbx-0xdf7b],cl
  400a7a:	ff 48 98             	dec    DWORD PTR [rax-0x68]
  400a7d:	0f b6 44 05 d0       	movzx  eax,BYTE PTR [rbp+rax*1-0x30]
  400a82:	66 98                	cbw
  400a84:	66 03 85 2e ff ff ff 	add    ax,WORD PTR [rbp-0xd2]
  400a8b:	83 e8 30             	sub    eax,0x30
  400a8e:	66 89 85 2e ff ff ff 	mov    WORD PTR [rbp-0xd2],ax
  400a95:	8b 85 20 ff ff ff    	mov    eax,DWORD PTR [rbp-0xe0]
  400a9b:	83 c0 04             	add    eax,0x4
  400a9e:	48 98                	cdqe
  400aa0:	0f b6 44 05 d0       	movzx  eax,BYTE PTR [rbp+rax*1-0x30]
  400aa5:	66 98                	cbw
  400aa7:	66 03 85 2c ff ff ff 	add    ax,WORD PTR [rbp-0xd4]
  400aae:	83 e8 30             	sub    eax,0x30
  400ab1:	66 89 85 2c ff ff ff 	mov    WORD PTR [rbp-0xd4],ax
  400ab8:	8b 85 20 ff ff ff    	mov    eax,DWORD PTR [rbp-0xe0]
  400abe:	83 c0 08             	add    eax,0x8
  400ac1:	48 98                	cdqe
  400ac3:	0f b6 44 05 d0       	movzx  eax,BYTE PTR [rbp+rax*1-0x30]
  400ac8:	66 98                	cbw
  400aca:	66 03 85 2a ff ff ff 	add    ax,WORD PTR [rbp-0xd6]
  400ad1:	83 e8 30             	sub    eax,0x30
  400ad4:	66 89 85 2a ff ff ff 	mov    WORD PTR [rbp-0xd6],ax
  400adb:	8b 85 20 ff ff ff    	mov    eax,DWORD PTR [rbp-0xe0]
  400ae1:	83 c0 0c             	add    eax,0xc
  400ae4:	48 98                	cdqe
  400ae6:	0f b6 44 05 d0       	movzx  eax,BYTE PTR [rbp+rax*1-0x30]
  400aeb:	66 98                	cbw
  400aed:	66 03 85 28 ff ff ff 	add    ax,WORD PTR [rbp-0xd8]
  400af4:	83 e8 30             	sub    eax,0x30
  400af7:	66 89 85 28 ff ff ff 	mov    WORD PTR [rbp-0xd8],ax
  400afe:	83 85 20 ff ff ff 01 	add    DWORD PTR [rbp-0xe0],0x1
  400b05:	83 bd 20 ff ff ff 03 	cmp    DWORD PTR [rbp-0xe0],0x3
  400b0c:	0f 8e 63 ff ff ff    	jle    0x400a75
  400b12:	eb 0f                	jmp    0x400b23
 
start:
  400b14:	48 8b 9d 10 ff ff ff 	mov    rbx,QWORD PTR [rbp-0xf0] ; anti_debug_1
  400b1b:	ff d3                	call   rbx  ; call anti_debug_1
  400b1d:	e9 41 ff ff ff       	jmp    0x400a63
  400b22:	e9 0f b7 95 2e       	jmp    0x2ed5c236
  400b27:	ff                   	(bad)
  400b28:	ff                   	(bad)
  400b29:	ff 0f                	dec    DWORD PTR [rdi]
  400b2b:	b7 85                	mov    bh,0x85
  400b2d:	2c ff                	sub    al,0xff
  400b2f:	ff                   	(bad)
  400b30:	ff 8d 0c 02 0f b7    	dec    DWORD PTR [rbp-0x48f0fdf4]
  400b36:	95                   	xchg   ebp,eax
  400b37:	2a ff                	sub    bh,bh
  400b39:	ff                   	(bad)
  400b3a:	ff 0f                	dec    DWORD PTR [rdi]
  400b3c:	b7 85                	mov    bh,0x85
  400b3e:	28 ff                	sub    bh,bh
  400b40:	ff                   	(bad)
  400b41:	ff 8d 04 02 01 c0    	dec    DWORD PTR [rbp-0x3ffefdfc]
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
