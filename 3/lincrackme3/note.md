IMPORTANT: Read the FOUND and TODOS:

We know the call to loc_400A59 has some trick.
The call to it, which is also the next instruction pushed to stack when calling, pop rax, + some offset,
pushed back to the stack for returning.
That's when we can't track normally anymore. 

We have 2 ways:
- Find the address after the adding offset, extract the binaries out, dumb the disassembly, still statically reversing.
- Patch both anti-debug functions, from conditional jumps to unconditional ones, and run gdb, set bp at loc_400A59,
and continue tracing from there.


https://copilot.microsoft.com/shares/1SoFsVbPHqw5DtrLyvu8v

ADDITIONAL: referencing the hasherezade's solution.


# FOUND:
OK, we've found that:
- loop_1 is to gen the values a, b, c, and d
- we go through some checks of them, if check fails, jmp to loop_2 and prints failure msg
- check success, we goes through the loop_3 to print the success msg.

# TODOS:
Let's analyze how the check algorithm works next time 

# Check algorithm:
    a, d are odd
    5 < d <= 24 ; d [7, 9, 11, 13, 15, 17, 19, 21, 23]
    c > b
    2a + 2b == d + c; d is odd, so c must be odd as well because the right hand side is 2(a+b) 
    
    We know that both d and a must be odd, so we can pick an easy path, a == d. Then we have
    c = 2b + a 
    
    So both a and d have the constraints in the allowed values, 7..23. Let's pick 7 for both.

    a = 7
    d = 7
    b = 3
    c = 13
         d    c    b    a
    => "1123-3712-0012-2311"


# STATIC analyze:
a = 0
b = 0
c = 0
d = 0

400b14:   48 8b 9d 10 ff ff ff    mov    rbx,QWORD PTR [rbp-0xf0] ; anti_debug_1                                          
400b1b:   ff d3                   call   rbx                      ; call anti_debug_1                                     
400b1d:   e9 41 ff ff ff          jmp    0x400a63

---

400a63:	48 89 c0             	mov    rax,rax
400a66:	c7 85 20 ff ff ff 00 	mov    DWORD PTR [rbp-i],0x0     ; i = 0 
400a6d:	00 00 00 
400a70:	e9 90 00 00 00       	jmp    0x400b05 

---

loop_1:
400a75:	8b 85 20 ff ff ff    	mov    eax,DWORD PTR [rbp-i]        ; i
400a7b:	48 98                	cdqe    
400a7d:	0f b6 44 05 d0       	movzx  eax,BYTE PTR [rbp+rax*1-s1]  ; x1 = s1[i]
400a82:	66 98                	cbw
400a84:	66 03 85 2e ff ff ff 	add    ax,WORD PTR [rbp-d]          ; x1 += d
400a8b:	83 e8 30             	sub    eax,0x30                     ; x1 -= 0x30
400a8e:	66 89 85 2e ff ff ff 	mov    WORD PTR [rbp-d],ax          ; d = x1


400a95:	8b 85 20 ff ff ff    	mov    eax,DWORD PTR [rbp-i]        ; i
400a9b:	83 c0 04             	add    eax,0x4                      ; i + 4         
400a9e:	48 98                	cdqe
400aa0:	0f b6 44 05 d0       	movzx  eax,BYTE PTR [rbp+rax*1-s1]  ; x2 = s1[i+4]
400aa5:	66 98                	cbw
400aa7:	66 03 85 2c ff ff ff 	add    ax,WORD PTR [rbp-c]          ; x2 += c
400aae:	83 e8 30             	sub    eax,0x30                     ; x2 -= 0x30
400ab1:	66 89 85 2c ff ff ff 	mov    WORD PTR [rbp-c],ax          ; c = x2 

400ab8:	8b 85 20 ff ff ff    	mov    eax,DWORD PTR [rbp-i]        ; i
400abe:	83 c0 08             	add    eax,0x8                      ; i + 8
400ac1:	48 98                	cdqe
400ac3:	0f b6 44 05 d0       	movzx  eax,BYTE PTR [rbp+rax*1-s1]  ; x3 = s1[i+8]
400ac8:	66 98                	cbw
400aca:	66 03 85 2a ff ff ff 	add    ax,WORD PTR [rbp-d]          ; x3 += b
400ad1:	83 e8 30             	sub    eax,0x30                     ; x3 -= 0x30
400ad4:	66 89 85 2a ff ff ff 	mov    WORD PTR [rbp-d],ax          ; b = x3

400adb:	8b 85 20 ff ff ff    	mov    eax,DWORD PTR [rbp-i]        ; i
400ae1:	83 c0 0c             	add    eax,0xc                      ; i + 0xc
400ae4:	48 98                	cdqe
400ae6:	0f b6 44 05 d0       	movzx  eax,BYTE PTR [rbp+rax*1-s1]  ; x4 = s1[i+0xc]
400aeb:	66 98                	cbw
400aed:	66 03 85 28 ff ff ff 	add    ax,WORD PTR [rbp-a]          ; x4 += a
400af4:	83 e8 30             	sub    eax,0x30                     ; x4 -= 0x30
400af7:	66 89 85 28 ff ff ff 	mov    WORD PTR [rbp-a],ax          ; a = x4

400afe:	83 85 20 ff ff ff 01 	add    DWORD PTR [rbp-i],0x1        ; i += 1
400b05:	83 bd 20 ff ff ff 03 	cmp    DWORD PTR [rbp-i],0x3        
400b0c:	0f 8e 63 ff ff ff    	jle    loop_1                       ; if i <= 3, back to loop
400b12:	eb 0f                	jmp    end_loop_1

---  

end_loop_1:
check_vars:
400b23:	0f b7 95 2e ff ff ff 	movzx  edx,WORD PTR [rbp-d]         ; d
400b2a:	0f b7 85 2c ff ff ff 	movzx  eax,WORD PTR [rbp-c]         ; c
400b31:	8d 0c 02             	lea    ecx,[rdx+rax*1]              ; d+c
400b34:	0f b7 95 2a ff ff ff 	movzx  edx,WORD PTR [rbp-b]         ; b
400b3b:	0f b7 85 28 ff ff ff 	movzx  eax,WORD PTR [rbp-a]         ; a
400b42:	8d 04 02             	lea    eax,[rdx+rax*1]              ; b+a
400b45:	01 c0                	add    eax,eax                      ; 2*(b+a)
400b47:	39 c1                	cmp    ecx,eax
400b49:	75 4a                	jne    end_check                    ; if 2*(b+a) != d+c, end_check

400b4b:	0f b7 85 2c ff ff ff 	movzx  eax,WORD PTR [rbp-c]         ; c 
400b52:	66 3b 85 2a ff ff ff 	cmp    ax,WORD PTR [rbp-b]          ; b
400b59:	76 3a                	jbe    end_check                    ; if c <= b, end_check

400b5b:	0f b7 95 2e ff ff ff 	movzx  edx,WORD PTR [rbp-d]         ; d
400b62:	0f b7 85 28 ff ff ff 	movzx  eax,WORD PTR [rbp-a]         ; a
400b69:	8d 04 02             	lea    eax,[rdx+rax*1]              ; d+a
400b6c:	83 e0 01             	and    eax,0x1                      ;
400b6f:	84 c0                	test   al,al                        ; (d+a) & 0x1 != 0?
400b71:	75 22                	jne    end_check                    ; if (d+a) is odd, end_check

400b73:	66 83 bd 2e ff ff ff 	cmp    WORD PTR [rbp-d],0x5         ; 
400b7a:	05          
400b7b:	76 18                	jbe    end_check                    ; if d <= 5, end_check

400b7d:	66 83 bd 2e ff ff ff 	cmp    WORD PTR [rbp-d],0x18        ; 
400b84:	18 
400b85:	77 0e                	ja     end_check                    ; if d > 0x18, end_check

400b87:	0f b7 85 28 ff ff ff 	movzx  eax,WORD PTR [rbp-a]         ; a
400b8e:	83 e0 01             	and    eax,0x1                      ; 
400b91:	85 c0                	test   eax,eax
400b93:	75 3f                	jne    0x400bd4                     ; if a is odd, jmp to 0x400bd4, else end_check

end_check:
400b95:	c7 85 1c ff ff ff 00 	mov    DWORD PTR [rbp-j],0x0        ; j = 0 
400b9c:	00 00 00 
400b9f:	eb 20                	jmp    0x400bc1                     ; jmp to loop_2_cond

---
loop_2: ; print: "Wrong key! I've seen monkeys smarter than you..."
400ba1:	8b 85 1c ff ff ff    	mov    eax,DWORD PTR [rbp-j]        ; j
400ba7:	48 98                	cdqe
400ba9:	0f b6 44 05 90       	movzx  eax,BYTE PTR [rbp+rax*1-s0]  ; y = s0[j]
400bae:	0f be c0             	movsx  eax,al                       ; 
400bb1:	34 e9                	xor    al,0xe9                      ; y ^= 0xe9
400bb3:	89 c7                	mov    edi,eax                      ; 
400bb5:	e8 ae fa ff ff       	call   putchar     ; putchar        ; putchar(y)
400bba:	83 85 1c ff ff ff 01 	add    DWORD PTR [rbp-j],0x1        ; j += 1

loop_2_cond:
400bc1:	83 bd 1c ff ff ff 31 	cmp    DWORD PTR [rbp-j],0x31       ; 
400bc8:	7e d7                	jle    loop_2                       ; if j <= 0x31, loop_2
400bca:	bf 01 00 00 00       	mov    edi,0x1                      ; 
400bcf:	e8 84 fa ff ff       	call   exit     ; exit

loop_2_end:
400bd4:	c7 85 18 ff ff ff 00 	mov    DWORD PTR [rbp-k],0x0        ; k = 0
400bdb:	00 00 00    
400bde:	eb 23                	jmp    0x400c03                     ; 

--- 
loop_3:
print_success:
400be0: 8b 85 18 ff ff ff       mov    eax,DWORD PTR [rbp-k]        ; k                                                 
400be6: 48 98                   cdqe                                                                                    
400be8: 0f b6 84 05 30 ff ff    movzx  eax,BYTE PTR [rbp+rax*1-s2]  ; z = s2[k]                                             
400bef: ff                                                                                                              
400bf0: 0f be c0                movsx  eax,al                                                                           
400bf3: 34 f9                   xor    al,0xf9                      ; z ^= 0xf9                                                    
400bf5: 89 c7                   mov    edi,eax                                                                          
400bf7: e8 6c fa ff ff          call   putchar                      ; putchar(z)                                                  
400bfc: 83 85 18 ff ff ff 01    add    DWORD PTR [rbp-k],0x1    

loop_3_cond:
400c03:	83 bd 18 ff ff ff 4f 	cmp    DWORD PTR [rbp-k],0x4f
400c0a:	7e d4                	jle    loop_3

ebd_pro:
400c0c:	b8 00 00 00 00       	mov    eax,0x0
400c11:	48 8b 55 e8          	mov    rdx,QWORD PTR [rbp-0x18]
400c15:	64 48 33 14 25 28 00 	xor    rdx,QWORD PTR fs:0x28
400c1c:	00 00 
400c1e:	74 05                	je     0x400c25
400c20:	e8 93 fa ff ff       	call   ___stack_chk_fail
400c25:	48 81 c4 e8 00 00 00 	add    rsp,0xe8
400c2c:	5b                   	pop    rbx
400c2d:	c9                   	leave
400c2e:	c3                   	ret
400c2f:	90                   	nop
