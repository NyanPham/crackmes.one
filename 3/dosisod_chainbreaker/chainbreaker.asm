 ; __int64 __fastcall parse(int, int, int)
.text:0000000000001215                 public _Z5parseiii
.text:0000000000001215 _Z5parseiii     proc near               ; CODE XREF: main+14D↓p
.text:0000000000001215
.text:0000000000001215 c               = dword ptr -1Ch
.text:0000000000001215 b               = dword ptr -18h
.text:0000000000001215 a               = dword ptr -14h
.text:0000000000001215 i               = dword ptr -8
.text:0000000000001215 x               = dword ptr -4
.text:0000000000001215
.text:0000000000001215 ; __unwind {
.text:0000000000001215                 push    rbp
.text:0000000000001216                 mov     rbp, rsp
.text:0000000000001219                 sub     rsp, 20h
.text:000000000000121D                 mov     [rbp+a], edi
.text:0000000000001220                 mov     [rbp+b], esi
.text:0000000000001223                 mov     [rbp+c], edx
.text:0000000000001226                 cmp     [rbp+b], 0
.text:0000000000001226 ; b != 0?
.text:000000000000122A                 jnz     short loc_1242
.text:000000000000122C ; b == 0:
.text:000000000000122C                 lea     rdi, s          ; "ERROR\nInvalid chain produced!"
.text:0000000000001233                 call    _puts
.text:0000000000001238                 mov     edi, 0          ; status
.text:000000000000123D                 call    _exit
.text:0000000000001242 ; ---------------------------------------------------------------------------
.text:0000000000001242 ; b != 0:
.text:0000000000001242
.text:0000000000001242 loc_1242:                               ; CODE XREF: parse(int,int,int)+15↑j
.text:0000000000001242                 cmp     [rbp+b], 0FFFFF000h
.text:0000000000001242 ; b < -4096?
.text:0000000000001249                 jl      short loc_1254
.text:000000000000124B ; b >= -4096:
.text:000000000000124B                 cmp     [rbp+b], 1000h
.text:000000000000124B ; b <= 4096?
.text:0000000000001252                 jle     short loc_1269
.text:0000000000001254 ; b > 4096:
.text:0000000000001254
.text:0000000000001254 ; b = -(b % 4096)
.text:0000000000001254
.text:0000000000001254 loc_1254:                               ; CODE XREF: parse(int,int,int)+34↑j
.text:0000000000001254                 mov     eax, [rbp+b]
.text:0000000000001257                 cdq
.text:0000000000001258                 shr     edx, 14h
.text:000000000000125B                 add     eax, edx
.text:000000000000125D                 and     eax, 0FFFh
.text:0000000000001262                 sub     eax, edx
.text:0000000000001264                 neg     eax
.text:0000000000001266                 mov     [rbp+b], eax
.text:0000000000001269
.text:0000000000001269 loc_1269:                               ; CODE XREF: parse(int,int,int)+3D↑j
.text:0000000000001269                 mov     [rbp+x], 1
.text:0000000000001270                 mov     [rbp+i], 0
.text:0000000000001277
.text:0000000000001277 loc_1277:                               ; CODE XREF: parse(int,int,int)+7B↓j
.text:0000000000001277                 cmp     [rbp+i], 2
.text:000000000000127B                 jg      short loc_1292
.text:000000000000127D                 mov     eax, [rbp+i]
.text:0000000000001280                 mov     edx, [rbp+b]
.text:0000000000001283                 mov     ecx, eax        ; i
.text:0000000000001285                 shl     edx, cl         ; b << i
.text:0000000000001287                 mov     eax, edx
.text:0000000000001289                 xor     [rbp+x], eax    ; x ^= b << i
.text:000000000000128C                 add     [rbp+i], 1      ; i += 1
.text:0000000000001290                 jmp     short loc_1277
.text:0000000000001292 ; ---------------------------------------------------------------------------
.text:0000000000001292
.text:0000000000001292 loc_1292:                               ; CODE XREF: parse(int,int,int)+66↑j
.text:0000000000001292                 mov     edx, [rbp+a]
.text:0000000000001295                 mov     eax, [rbp+c]
.text:0000000000001298                 add     eax, edx
.text:000000000000129A                 sub     eax, 1          ; a + c - 1
.text:000000000000129D                 xor     eax, [rbp+b]    ; (a + c - 1) ^ b
.text:00000000000012A0                 mov     edx, eax
.text:00000000000012A2                 mov     eax, [rbp+x]
.text:00000000000012A5                 add     edx, eax        ; x + ((a + c - 1) ^ b)
.text:00000000000012A7                 mov     eax, [rbp+a]
.text:00000000000012AA                 add     eax, edx        ; x + ((a + c - 1) ^ b) + a
.text:00000000000012AC                 sub     eax, 0Fh        ; ret = x + ((a + c - 1) ^ b) + a - 15
.text:00000000000012AF                 leave
.text:00000000000012B0                 retn
.text:00000000000012B0 ; } // starts at 1215
.text:00000000000012B0 _Z5parseiii     endp

.text:00000000000012B1 ; int __fastcall main(int argc, const char **argv, const char **envp)
.text:00000000000012B1                 public main
.text:00000000000012B1 main            proc near               ; DATA XREF: _start+1D↑o
.text:00000000000012B1
.text:00000000000012B1 argv            = qword ptr -80h
.text:00000000000012B1 argc            = dword ptr -74h
.text:00000000000012B1 sleep_time      = dword ptr -64h
.text:00000000000012B1 seed_str        = byte ptr -60h
.text:00000000000012B1 salloc_0        = byte ptr -31h
.text:00000000000012B1 dur_ms          = byte ptr -30h
.text:00000000000012B1 seed            = dword ptr -24h
.text:00000000000012B1 unk_int         = dword ptr -20h
.text:00000000000012B1 i               = dword ptr -1Ch
.text:00000000000012B1 r               = dword ptr -18h
.text:00000000000012B1 next_seed       = dword ptr -14h
.text:00000000000012B1
.text:00000000000012B1 ; __unwind { // __gxx_personality_v0
.text:00000000000012B1                 push    rbp
.text:00000000000012B2                 mov     rbp, rsp
.text:00000000000012B5                 push    rbx
.text:00000000000012B6                 sub     rsp, 78h
.text:00000000000012BA                 mov     [rbp+argc], edi
.text:00000000000012BD                 mov     [rbp+argv], rsi
.text:00000000000012C1                 mov     [rbp+unk_int], 64h ; 'd'
.text:00000000000012C1
.text:00000000000012C1
.text:00000000000012C8                 cmp     [rbp+argc], 2
.text:00000000000012C8 ; argc != 2?
.text:00000000000012CC                 jnz     wrong_usage
.text:00000000000012D2 ; argc == 2:
.text:00000000000012D2                 lea     rdi, aStartingChainb ; "Starting chainbreaker!"
.text:00000000000012D9                 call    _puts
.text:00000000000012D9
.text:00000000000012D9
.text:00000000000012DE                 lea     rax, [rbp+salloc_0]
.text:00000000000012E2                 mov     rdi, rax
.text:00000000000012E5                 call    __ZNSaIcEC1Ev   ; std::allocator<char>::allocator(void)
.text:00000000000012E5
.text:00000000000012E5
.text:00000000000012EA ; seed_str = std::string(argv[1], salloc_0)
.text:00000000000012EA                 mov     rax, [rbp+argv]
.text:00000000000012EE                 add     rax, 8
.text:00000000000012F2                 mov     rcx, [rax]      ; argv[1]
.text:00000000000012F5                 lea     rdx, [rbp+salloc_0]
.text:00000000000012F9                 lea     rax, [rbp+seed_str]
.text:00000000000012FD                 mov     rsi, rcx        ; argv[1]
.text:0000000000001300                 mov     rdi, rax
.text:0000000000001303 ;   try {
.text:0000000000001303                 call    __ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_ ; std::string::basic_string(char const*,std::allocator<char> const&)
.text:0000000000001303 ;   } // starts at 1303
.text:0000000000001303
.text:0000000000001303
.text:0000000000001308 ; seed = stoi(seed_str, nulptr=0, base=10)
.text:0000000000001308                 lea     rax, [rbp+seed_str]
.text:000000000000130C                 mov     edx, 0Ah
.text:0000000000001311                 mov     esi, 0
.text:0000000000001316                 mov     rdi, rax        ; seed_str
.text:0000000000001319 ;   try {
.text:0000000000001319                 call    _ZNSt7__cxx114stoiERKNS_12basic_stringIcSt11char_traitsIcESaIcEEEPmi ; std::stoi(std::string const&,ulong *,int)
.text:0000000000001319 ;   } // starts at 1319
.text:000000000000131E                 mov     [rbp+seed], eax
.text:000000000000131E
.text:000000000000131E
.text:0000000000001321 ; ~seed_str()
.text:0000000000001321 ; ~salloc_0()
.text:0000000000001321                 lea     rax, [rbp+seed_str]
.text:0000000000001325                 mov     rdi, rax
.text:0000000000001328                 call    __ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev ; std::string::~string()
.text:000000000000132D                 lea     rax, [rbp+salloc_0]
.text:0000000000001331                 mov     rdi, rax
.text:0000000000001334                 call    __ZNSaIcED1Ev   ; std::allocator<char>::~allocator()
.text:0000000000001334
.text:0000000000001334
.text:0000000000001339                 mov     eax, [rbp+seed]
.text:000000000000133C                 mov     [rbp+next_seed], eax ; next_seed = seed
.text:000000000000133C
.text:000000000000133C
.text:000000000000133F ; r = (((seed ^ 0x7b) + (seed ^ 0x141)) * 0x533d) / 100
.text:000000000000133F ; x = (((seed ^ 0x7b) + (seed ^ 0x141)) * 0x533d)
.text:000000000000133F                 mov     eax, [rbp+seed]
.text:0000000000001342                 xor     eax, 7Bh        ; seed ^ 0x7b
.text:0000000000001345                 mov     edx, eax        ; seed ^ 0x7b
.text:0000000000001347                 mov     eax, [rbp+seed]
.text:000000000000134A                 xor     eax, 141h       ; seed ^ 0x141
.text:000000000000134F                 add     eax, edx        ; (seed ^ 0x7b) + (seed ^ 0x141)
.text:0000000000001351                 imul    ecx, eax, 533Dh ; x = ((seed ^ 0x7b) + (seed ^ 0x141)) * 0x533d
.text:0000000000001357                 mov     edx, 51EB851Fh  ; 0x51eb851f
.text:000000000000135C                 mov     eax, ecx
.text:000000000000135E                 imul    edx             ; x * 0x51eb851f
.text:0000000000001360                 sar     edx, 5
.text:0000000000001363                 mov     eax, ecx
.text:0000000000001365                 sar     eax, 1Fh
.text:0000000000001368                 sub     edx, eax
.text:000000000000136A                 mov     eax, edx
.text:000000000000136C                 mov     [rbp+r], eax    ; res = x / 100 (truncate toward zero)
.text:000000000000136C
.text:000000000000136C
.text:000000000000136F                 mov     eax, [rbp+r]
.text:0000000000001372                 imul    eax, 64h ; 'd'
.text:0000000000001375                 sub     ecx, eax
.text:0000000000001377                 mov     eax, ecx
.text:0000000000001379                 mov     [rbp+r], eax    ; r = x - (res * 100)
.text:0000000000001379
.text:0000000000001379
.text:000000000000137C                 cmp     [rbp+r], 0
.text:000000000000137C ; r >= 0?
.text:0000000000001380                 jns     short loc_1387
.text:0000000000001382 ; r < 0:
.text:0000000000001382                 neg     [rbp+r]         ; r = -r
.text:0000000000001385                 jmp     short loc_1394
.text:0000000000001387 ; ---------------------------------------------------------------------------
.text:0000000000001387 ; r >= 0:
.text:0000000000001387
.text:0000000000001387 loc_1387:                               ; CODE XREF: main+CF↑j
.text:0000000000001387                 cmp     [rbp+r], 0
.text:0000000000001387 ; r != 0?
.text:000000000000138B                 jnz     short loc_1394
.text:000000000000138D ; r == 0:
.text:000000000000138D                 mov     [rbp+r], 0Ah    ; r = 10
.text:0000000000001394
.text:0000000000001394 loc_1394:                               ; CODE XREF: main+D4↑j
.text:0000000000001394                                         ; main+DA↑j
.text:0000000000001394                 mov     rax, [rbp+argv]
.text:0000000000001398                 add     rax, 8
.text:000000000000139C                 mov     rax, [rax]      ; seed_str -- argv[1]
.text:000000000000139F                 mov     edx, [rbp+r]
.text:00000000000013A2                 mov     rsi, rax
.text:00000000000013A5                 lea     rdi, format     ; "Seed %s requires %d links\n\n"
.text:00000000000013AC                 mov     eax, 0
.text:00000000000013B1                 call    _printf         ; printf("Seed %s requires %d links\n\n", seed_str, r)
.text:00000000000013B1
.text:00000000000013B1
.text:00000000000013B6                 mov     [rbp+i], 0
.text:00000000000013BD
.text:00000000000013BD loc_13BD:                               ; CODE XREF: main+1A5↓j
.text:00000000000013BD                 cmp     [rbp+i], 63h ; 'c'
.text:00000000000013BD ; i > 99?
.text:00000000000013C1                 jg      loc_145B
.text:00000000000013C7                 mov     eax, [rbp+i]
.text:00000000000013CA                 cmp     eax, [rbp+r]
.text:00000000000013CA ; i >= r?
.text:00000000000013CD                 jge     loc_145B
.text:00000000000013D3 ; i < r:
.text:00000000000013D3                 mov     eax, [rbp+i]
.text:00000000000013D6                 lea     ecx, [rax+1]    ; i+1
.text:00000000000013D9                 mov     eax, [rbp+next_seed]
.text:00000000000013DC                 mov     edx, eax
.text:00000000000013DE                 mov     esi, ecx
.text:00000000000013E0                 lea     rdi, aLinkDD    ; "LINK %d\t\t%d\t->\t"
.text:00000000000013E7                 mov     eax, 0
.text:00000000000013EC                 call    _printf         ; printf("LINK %d\t\t%d->\t", i+1, next_seed)
.text:00000000000013F1                 mov     edx, [rbp+i]    ; int
.text:00000000000013F4                 mov     ecx, [rbp+next_seed]
.text:00000000000013F7                 mov     eax, [rbp+seed]
.text:00000000000013FA                 mov     esi, ecx        ; int
.text:00000000000013FC                 mov     edi, eax        ; int
.text:00000000000013FE                 call    _Z5parseiii     ; parse(int,int,int)
.text:0000000000001403                 mov     [rbp+next_seed], eax ; next_seed = parse(seed, next_seed, i)
.text:0000000000001406                 mov     eax, [rbp+next_seed]
.text:0000000000001409                 mov     [rbp+sleep_time], eax ; sleep_time = next_seed
.text:000000000000140C                 mov     eax, [rbp+sleep_time]
.text:000000000000140F                 test    eax, eax
.text:000000000000140F ; sleep_time >= 0?
.text:0000000000001411                 jns     short loc_141A
.text:0000000000001413 ; sleep_time < 0?
.text:0000000000001413                 mov     [rbp+sleep_time], 0 ; sleep_time = 0
.text:000000000000141A
.text:000000000000141A loc_141A:                               ; CODE XREF: main+160↑j
.text:000000000000141A                 mov     edx, [rbp+sleep_time]
.text:000000000000141D                 mov     eax, [rbp+next_seed]
.text:0000000000001420                 mov     esi, eax
.text:0000000000001422                 lea     rdi, aDSleepingForDm ; "%d\t Sleeping for %dms\n"
.text:0000000000001429                 mov     eax, 0
.text:000000000000142E                 call    _printf         ; printf("%d\t Sleeping for %dms\n", next_seed, sleep_time)
.text:0000000000001433                 lea     rdx, [rbp+sleep_time]
.text:0000000000001437                 lea     rax, [rbp+dur_ms]
.text:000000000000143B                 mov     rsi, rdx
.text:000000000000143E                 mov     rdi, rax
.text:0000000000001441                 call    _ZNSt6chrono8durationIlSt5ratioILl1ELl1000EEEC2IivEERKT_ ; std::chrono::duration<long,std::ratio<1l,1000l>>::duration<int,void>(int const&)
.text:0000000000001446                 lea     rax, [rbp+dur_ms]
.text:000000000000144A                 mov     rdi, rax
.text:000000000000144D                 call    _ZNSt11this_thread9sleep_forIlSt5ratioILl1ELl1000EEEEvRKNSt6chrono8durationIT_T0_EE ; std::this_thread::sleep_for<long,std::ratio<1l,1000l>>(std::chrono::duration<long,std::ratio<1l,1000l>> const&)
.text:0000000000001452                 add     [rbp+i], 1      ; i++
.text:0000000000001456                 jmp     loc_13BD
.text:000000000000145B ; ---------------------------------------------------------------------------
.text:000000000000145B ; i > 99 || i >= r?
.text:000000000000145B
.text:000000000000145B loc_145B:                               ; CODE XREF: main+110↑j
.text:000000000000145B                                         ; main+11C↑j
.text:000000000000145B                 cmp     [rbp+i], 63h ; 'c'
.text:000000000000145B ; i != 99?
.text:000000000000145F                 jnz     short loc_1477
.text:0000000000001461 ; i == 99:
.text:0000000000001461                 lea     rdi, aErrorMaximumAl ; "ERROR\nMaximum allowed iterations reach"...
.text:0000000000001468                 call    _puts
.text:000000000000146D                 mov     edi, 1          ; status
.text:0000000000001472                 call    _exit
.text:0000000000001477 ; ---------------------------------------------------------------------------
.text:0000000000001477 ; i > 99:
.text:0000000000001477
.text:0000000000001477 loc_1477:                               ; CODE XREF: main+1AE↑j
.text:0000000000001477                 mov     eax, [rbp+seed]
.text:000000000000147A                 cmp     eax, [rbp+next_seed]
.text:000000000000147A ; seed != next_seed?
.text:000000000000147D                 jnz     short failure_match_seed
.text:000000000000147F                 mov     eax, [rbp+i]
.text:0000000000001482                 cmp     eax, [rbp+r]
.text:0000000000001482 ; i != r?
.text:0000000000001485                 jnz     short failure_match_seed
.text:0000000000001487 ; i == r:
.text:0000000000001487 ; success:
.text:0000000000001487                 lea     rdi, aYouHaveBrokenT ; "You have broken the chain!"
.text:000000000000148E                 call    _puts
.text:0000000000001493                 mov     edi, 0          ; status
.text:0000000000001498                 call    _exit
.text:000000000000149D ; ---------------------------------------------------------------------------
.text:000000000000149D
.text:000000000000149D failure_match_seed:                     ; CODE XREF: main+1CC↑j
.text:000000000000149D                                         ; main+1D4↑j
.text:000000000000149D                 lea     rdi, aErrorStartingS ; "ERROR\nStarting seed doesnt match final"...
.text:00000000000014A4                 call    _puts
.text:00000000000014A9                 jmp     short loc_14B7
.text:00000000000014AB ; ---------------------------------------------------------------------------
.text:00000000000014AB
.text:00000000000014AB wrong_usage:                            ; CODE XREF: main+1B↑j
.text:00000000000014AB                 lea     rdi, aUsageChainbrea ; "usage: ./chainbreaker SEED"
.text:00000000000014B2                 call    _puts
.text:00000000000014B7
.text:00000000000014B7 loc_14B7:                               ; CODE XREF: main+1F8↑j
.text:00000000000014B7                 mov     eax, 0
.text:00000000000014BC                 jmp     short loc_1512
.text:00000000000014BE ; ---------------------------------------------------------------------------
.text:00000000000014BE ;   cleanup() // owned by 1319
.text:00000000000014BE                 mov     rbx, rax
.text:00000000000014C1                 lea     rax, [rbp+seed_str]
.text:00000000000014C5                 mov     rdi, rax
.text:00000000000014C8                 call    __ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev ; std::string::~string()
.text:00000000000014CD                 jmp     short loc_14D2
.text:00000000000014CF ; ---------------------------------------------------------------------------
.text:00000000000014CF ;   cleanup() // owned by 1303
.text:00000000000014CF                 mov     rbx, rax
.text:00000000000014D2
.text:00000000000014D2 loc_14D2:                               ; CODE XREF: main+21C↑j
.text:00000000000014D2                 lea     rax, [rbp+salloc_0]
.text:00000000000014D6                 mov     rdi, rax
.text:00000000000014D9                 call    __ZNSaIcED1Ev   ; std::allocator<char>::~allocator()
.text:00000000000014DE                 mov     rax, rbx
.text:00000000000014E1                 mov     rdi, rax        ; void *
.text:00000000000014E4                 call    ___cxa_begin_catch
.text:00000000000014E9                 lea     rdi, aErrorSeedMustB ; "ERROR\nSeed must be an integer!"
.text:00000000000014F0 ;   try {
.text:00000000000014F0                 call    _puts
.text:00000000000014F0 ;   } // starts at 14F0
.text:00000000000014F5                 mov     edi, 0          ; status
.text:00000000000014FA                 call    _exit
.text:00000000000014FF ; ---------------------------------------------------------------------------
.text:00000000000014FF ;   cleanup() // owned by 14F0
.text:00000000000014FF                 mov     rbx, rax
.text:0000000000001502                 call    ___cxa_end_catch
.text:0000000000001507                 mov     rax, rbx
.text:000000000000150A                 mov     rdi, rax        ; struct _Unwind_Exception *
.text:000000000000150D                 call    __Unwind_Resume
.text:0000000000001512 ; ---------------------------------------------------------------------------
.text:0000000000001512
.text:0000000000001512 loc_1512:                               ; CODE XREF: main+20B↑j
.text:0000000000001512                 add     rsp, 78h
.text:0000000000001516                 pop     rbx
.text:0000000000001517                 pop     rbp
.text:0000000000001518                 retn
.text:0000000000001518 ; } // starts at 12B1
.text:0000000000001518 main            endp
