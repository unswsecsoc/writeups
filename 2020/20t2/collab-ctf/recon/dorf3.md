# dorf3

## Authors
* Abiram Nadarajah (@abiramen)

## Category
* Recon

## Description
i hope he didnt take any company files before i fired him !
## Difficulty
* hard

## Points
100

## Solution
<details>
<summary>spoiler</summary>

### Idea
Inspect commit histories for hidden secrets

### Walkthrough
1. Check the stars on the GitHub profile found in dorf3.
2. Find the GitHub profile for the fired employee, Rob.
3. Inspect the four repos which are on the profile. Three of them have only commits, but one repo contains ~10 commits.
4. Inspect each of the commits, most with unsuspicious messages, to find an SSH private key, and an OpenSSH Config file containing a username and a host IP address.
5. Download the SSH key to use as an identity file, and use the command `ssh rob@IP -i ~/path/to/downloaded/key` to gain access to a shell on Rob's server.
6. Use `ls` to see what folders exist, and `cd` to the folder containing work files.
7. Use `grep FLAG *.txt` to find the file containing the flag.

### Flag
`FLAG{5teAling_sEcr3Ts_is_rUd3_bUt_d0Nt_puBlisH_thEm}`
</details>
