# G@ldfish

## Authors
* p1gc0rn

## Category
* Forensics

## Tags
* MacOSX

## Description
I have a gold fish brain as I keep forgetting  important things. I need to use my email address now but I dont remember where I left it :( Could you find it for me?

## Difficulty
* easy

## Points
100

## Hints
1. Contacts application

## Files
* mem.raw [800mb download here](https://drive.google.com/file/d/1-t9-2uXzVjPghOVYP_K2jYyMOYj0r82Z/view?usp=sharing)
* MacSierra_10_12_16A323x64 (profile file for volatility)

## Solution
<details>
<summary>spoiler</summary>

### Idea
MacOS memory dump contains contents of current users including email addresses. Using volatility  or strings to extract the application and find the email address.

### Walkthrough
Strings and grep will take a while to search for. The strategy is looking for the current user's name (Alice), and then grep part of the email to figure out.

Volatility
1. Put profile file into volatility/plugins/overlays/mac/
2. Check volatility recognise the profile or not:
`python volatility/vol.py -f mem.raw mac_get_profile`
3. Check the process of Contacts application:
`python volatility/vol.py --profile=MacSierra_10_12_16A323x64 -f mem.raw mac_pslist | grep Contacts`
4. Extract contents of Contacts application, there is Alice's record:
`python volatility/vol.py --profile=MacSierra_10_12_16A323x64 -f mem.raw mac_contacts -p 261`
5. Find the email address of Alice with mac_yarascan
`python volatility/vol.py --profile=MacSierra_10_12_16A323x64 -f Downloads/mem.raw mac_yarascan -Y "alice" -p 261`

### Flag
`ATLASSIAN{hello@neverland.com}`
</details>
