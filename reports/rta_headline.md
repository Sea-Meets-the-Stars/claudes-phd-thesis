# RT-A headline numbers (peek)

Generated 2026-09-17 08:28 by `claudes_phd_thesis/scripts/rta_headline.py` from the IOPtics stage-2 metrics under `$OS_COLOR/IOPtics/runs/`.  The IOPtics report stage has not run; treat these as provisional.

## L23 (X=4, PACE noise, 3,320 spectra) — `rt_tests_A_l23_v1`

### Fit quality, mcmc

| variant | n_attempted | frac_ok | frac_poor_fit | frac_out_of_scope | chi2_nu median | rel_misfit median |
|---|---|---|---|---|---|---|
| expb_pow_ztt_el | 3320 | 0.994 | 0.003 | 0.003 | 1.12 | 0.096 |
| expb_pow_hyb_el | 3320 | 0.994 | 0.003 | 0.003 | 1.14 | 0.098 |
| expb_pow_hyb_ram | 3320 | 0.994 | 0.003 | 0.003 | 1.14 | 0.099 |
| expb_pow_hyb_ramfl | 3320 | 0.997 | 0.000 | 0.003 | 1.07 | 0.096 |
| expb_pow_hyb_ramflcdom | 3320 | 0.997 | 0.000 | 0.003 | 1.08 | 0.097 |

### Accuracy vs truth, mcmc (MAE and bias are fractional, log-space; cov68 nominal 0.68)

| variant | a(440) MAE / bias / cov68 | a_ph(440) MAE / bias / cov68 | a_dg(440) MAE / bias / cov68 | bb_p(555) MAE / bias / cov68 | bb_p(670) MAE / bias / cov68 |
|---|---|---|---|---|---|
| expb_pow_ztt_el | 0.053 / 0.028 / 0.66 (n=3300) | 0.908 / -0.331 / 0.64 (n=3300) | 0.255 / 0.064 / 0.63 (n=3300) | 0.547 / 0.547 / 0.00 (n=3300) | 0.676 / 0.676 / 0.00 (n=3300) |
| expb_pow_hyb_el | 0.052 / 0.032 / 0.62 (n=3300) | 1.351 / -0.483 / 0.58 (n=3300) | 0.285 / 0.140 / 0.60 (n=3300) | 0.414 / 0.414 / 0.02 (n=3300) | 0.601 / 0.601 / 0.00 (n=3300) |
| expb_pow_hyb_ram | 0.051 / 0.036 / 0.60 (n=3300) | 2.520 / -0.689 / 0.49 (n=3300) | 0.376 / 0.306 / 0.43 (n=3300) | 0.123 / 0.096 / 0.52 (n=3300) | 0.263 / 0.258 / 0.24 (n=3300) |
| expb_pow_hyb_ramfl | 0.059 / 0.049 / 0.59 (n=3309) | 0.846 / -0.376 / 0.61 (n=3309) | 0.261 / 0.200 / 0.56 (n=3309) | 0.104 / 0.057 / 0.63 (n=3309) | 0.179 / 0.163 / 0.48 (n=3309) |
| expb_pow_hyb_ramflcdom | 0.050 / 0.028 / 0.70 (n=3309) | 0.925 / -0.404 / 0.59 (n=3309) | 0.248 / 0.168 / 0.57 (n=3309) | 0.116 / -0.049 / 0.59 (n=3309) | 0.134 / 0.058 / 0.66 (n=3309) |

### Fit quality, chisq

| variant | n_attempted | frac_ok | frac_poor_fit | frac_out_of_scope | chi2_nu median | rel_misfit median |
|---|---|---|---|---|---|---|
| expb_pow_ztt_el | 3320 | 0.994 | 0.003 | 0.003 | 1.09 | 0.096 |
| expb_pow_hyb_el | 3320 | 0.994 | 0.003 | 0.003 | 1.09 | 0.096 |
| expb_pow_hyb_ram | 3320 | 0.994 | 0.003 | 0.003 | 1.08 | 0.096 |
| expb_pow_hyb_ramfl | 3320 | 0.997 | 0.000 | 0.003 | 1.02 | 0.094 |
| expb_pow_hyb_ramflcdom | 3320 | 0.997 | 0.000 | 0.003 | 1.02 | 0.094 |

### Accuracy vs truth, chisq (MAE and bias are fractional, log-space; cov68 nominal 0.68)

| variant | a(440) MAE / bias / cov68 | a_ph(440) MAE / bias / cov68 | a_dg(440) MAE / bias / cov68 | bb_p(555) MAE / bias / cov68 | bb_p(670) MAE / bias / cov68 |
|---|---|---|---|---|---|
| expb_pow_ztt_el | 0.093 / 0.057 / 0.53 (n=3300) | 0.651 / 0.051 / 0.89 (n=3300) | 0.322 / -0.075 / 0.95 (n=3300) | 0.498 / 0.498 / 0.04 (n=3300) | 0.679 / 0.679 / 0.02 (n=3300) |
| expb_pow_hyb_el | 0.069 / 0.023 / 0.62 (n=3300) | 0.717 / -0.151 / 0.92 (n=3300) | 0.321 / -0.018 / 0.91 (n=3300) | 0.421 / 0.420 / 0.32 (n=3300) | 0.685 / 0.685 / 0.06 (n=3300) |
| expb_pow_hyb_ram | 0.062 / 0.028 / 0.66 (n=3300) | 1.140 / -0.449 / 0.95 (n=3300) | 0.340 / 0.203 / 0.81 (n=3300) | 0.162 / 0.142 / 0.80 (n=3300) | 0.385 / 0.381 / 0.39 (n=3300) |
| expb_pow_hyb_ramfl | 0.091 / 0.067 / 0.75 (n=3309) | 0.559 / -0.150 / 0.85 (n=3309) | 0.307 / 0.116 / 0.89 (n=3309) | 0.140 / 0.099 / 0.85 (n=3309) | 0.250 / 0.229 / 0.63 (n=3309) |
| expb_pow_hyb_ramflcdom | 0.074 / 0.037 / 0.80 (n=3309) | 0.601 / -0.178 / 0.85 (n=3309) | 0.290 / 0.063 / 0.89 (n=3309) | 0.123 / -0.002 / 0.85 (n=3309) | 0.204 / 0.146 / 0.74 (n=3309) |

### Model selection (delta-BIC), configured contest

| fit | model_a (more complex) | model_b | n | frac favour a | frac favour b | median dBIC |
|---|---|---|---|---|---|---|
| chisq | expb_pow_hyb_el | expb_pow_hyb_ram | 3300 | 0.446 | 0.554 | 0.2 |
| chisq | expb_pow_hyb_el | expb_pow_hyb_ramfl | 3300 | 0.172 | 0.828 | 2.8 |
| chisq | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 3300 | 0.196 | 0.804 | 2.7 |
| chisq | expb_pow_hyb_el | expb_pow_ztt_el | 3300 | 0.499 | 0.501 | 0.0 |
| chisq | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 3300 | 0.197 | 0.803 | 1.4 |
| chisq | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 3300 | 0.224 | 0.776 | 1.3 |
| chisq | expb_pow_hyb_ram | expb_pow_ztt_el | 3300 | 0.540 | 0.460 | -0.3 |
| chisq | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 3309 | 0.610 | 0.390 | -0.1 |
| chisq | expb_pow_hyb_ramfl | expb_pow_ztt_el | 3300 | 0.812 | 0.188 | -3.0 |
| chisq | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | 3300 | 0.786 | 0.214 | -2.9 |
| mcmc | expb_pow_hyb_el | expb_pow_hyb_ram | 3300 | 0.566 | 0.434 | -0.3 |
| mcmc | expb_pow_hyb_el | expb_pow_hyb_ramfl | 3300 | 0.252 | 0.748 | 2.5 |
| mcmc | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 3300 | 0.294 | 0.706 | 2.1 |
| mcmc | expb_pow_hyb_el | expb_pow_ztt_el | 3300 | 0.386 | 0.614 | 0.4 |
| mcmc | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 3300 | 0.188 | 0.812 | 1.9 |
| mcmc | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 3300 | 0.256 | 0.744 | 1.5 |
| mcmc | expb_pow_hyb_ram | expb_pow_ztt_el | 3300 | 0.382 | 0.618 | 0.9 |
| mcmc | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 3309 | 0.693 | 0.307 | -0.4 |
| mcmc | expb_pow_hyb_ramfl | expb_pow_ztt_el | 3300 | 0.700 | 0.300 | -2.1 |
| mcmc | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | 3300 | 0.653 | 0.347 | -1.7 |

### Head-to-head, mcmc (paired bootstrap, 10% equivalence floor)

| component | ref_wave | model_a | model_b | delta MAE (a - b) | 95% CI | verdict |
|---|---|---|---|---|---|---|
| a | 440 | expb_pow_hyb_el | expb_pow_hyb_ram | 0.0013 | [0.0006, 0.0019] | indistinguishable |
| a | 440 | expb_pow_hyb_el | expb_pow_hyb_ramfl | -0.0059 | [-0.0073, -0.0046] | indistinguishable |
| a | 440 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.0034 | [0.0021, 0.0046] | indistinguishable |
| a | 440 | expb_pow_hyb_el | expb_pow_ztt_el | -0.0010 | [-0.0018, -0.0002] | indistinguishable |
| a | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | -0.0071 | [-0.0082, -0.0060] | indistinguishable |
| a | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 0.0021 | [0.0011, 0.0032] | indistinguishable |
| a | 440 | expb_pow_hyb_ram | expb_pow_ztt_el | -0.0023 | [-0.0033, -0.0013] | indistinguishable |
| a | 440 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 0.0092 | [0.0085, 0.0099] | indistinguishable |
| a | 440 | expb_pow_hyb_ramfl | expb_pow_ztt_el | 0.0049 | [0.0034, 0.0064] | indistinguishable |
| a | 440 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -0.0044 | [-0.0058, -0.0029] | indistinguishable |
| a | 443 | expb_pow_hyb_el | expb_pow_hyb_ram | 0.0019 | [0.0013, 0.0025] | indistinguishable |
| a | 443 | expb_pow_hyb_el | expb_pow_hyb_ramfl | -0.0043 | [-0.0054, -0.0031] | indistinguishable |
| a | 443 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.0043 | [0.0030, 0.0054] | indistinguishable |
| a | 443 | expb_pow_hyb_el | expb_pow_ztt_el | -0.0004 | [-0.0012, 0.0004] | indistinguishable |
| a | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | -0.0062 | [-0.0072, -0.0052] | indistinguishable |
| a | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 0.0024 | [0.0013, 0.0035] | indistinguishable |
| a | 443 | expb_pow_hyb_ram | expb_pow_ztt_el | -0.0023 | [-0.0033, -0.0013] | indistinguishable |
| a | 443 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 0.0085 | [0.0078, 0.0092] | indistinguishable |
| a | 443 | expb_pow_hyb_ramfl | expb_pow_ztt_el | 0.0039 | [0.0024, 0.0053] | indistinguishable |
| a | 443 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -0.0047 | [-0.0061, -0.0034] | indistinguishable |
| a_ph | 440 | expb_pow_hyb_el | expb_pow_hyb_ram | -1.1693 | [-1.2810, -1.0707] | expb_pow_hyb_el |
| a_ph | 440 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 0.5026 | [0.4034, 0.6069] | expb_pow_hyb_ramfl |
| a_ph | 440 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.4229 | [0.3145, 0.5300] | expb_pow_hyb_ramflcdom |
| a_ph | 440 | expb_pow_hyb_el | expb_pow_ztt_el | 0.4425 | [0.3877, 0.4980] | expb_pow_ztt_el |
| a_ph | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 1.6719 | [1.5013, 1.8547] | expb_pow_hyb_ramfl |
| a_ph | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 1.5922 | [1.4278, 1.7638] | expb_pow_hyb_ramflcdom |
| a_ph | 440 | expb_pow_hyb_ram | expb_pow_ztt_el | 1.6118 | [1.4760, 1.7554] | expb_pow_ztt_el |
| a_ph | 440 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | -0.0794 | [-0.0908, -0.0688] | indistinguishable |
| a_ph | 440 | expb_pow_hyb_ramfl | expb_pow_ztt_el | -0.0601 | [-0.1271, 0.0076] | underpowered |
| a_ph | 440 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | 0.0196 | [-0.0547, 0.0980] | indistinguishable |
| a_ph | 443 | expb_pow_hyb_el | expb_pow_hyb_ram | -1.0934 | [-1.1938, -1.0013] | expb_pow_hyb_el |
| a_ph | 443 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 0.4944 | [0.3937, 0.6102] | expb_pow_hyb_ramfl |
| a_ph | 443 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.4197 | [0.3227, 0.5296] | expb_pow_hyb_ramflcdom |
| a_ph | 443 | expb_pow_hyb_el | expb_pow_ztt_el | 0.4242 | [0.3716, 0.4777] | expb_pow_ztt_el |
| a_ph | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 1.5877 | [1.4364, 1.7482] | expb_pow_hyb_ramfl |
| a_ph | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 1.5130 | [1.3570, 1.6857] | expb_pow_hyb_ramflcdom |
| a_ph | 443 | expb_pow_hyb_ram | expb_pow_ztt_el | 1.5175 | [1.3827, 1.6703] | expb_pow_ztt_el |
| a_ph | 443 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | -0.0744 | [-0.0852, -0.0635] | indistinguishable |
| a_ph | 443 | expb_pow_hyb_ramfl | expb_pow_ztt_el | -0.0702 | [-0.1423, -0.0014] | underpowered |
| a_ph | 443 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | 0.0045 | [-0.0740, 0.0729] | indistinguishable |
| a_dg | 440 | expb_pow_hyb_el | expb_pow_hyb_ram | -0.0907 | [-0.0968, -0.0849] | indistinguishable |
| a_dg | 440 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 0.0255 | [0.0131, 0.0392] | indistinguishable |
| a_dg | 440 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.0388 | [0.0271, 0.0528] | indistinguishable |
| a_dg | 440 | expb_pow_hyb_el | expb_pow_ztt_el | 0.0301 | [0.0236, 0.0353] | indistinguishable |
| a_dg | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 0.1162 | [0.1046, 0.1295] | expb_pow_hyb_ramfl |
| a_dg | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 0.1294 | [0.1174, 0.1431] | expb_pow_hyb_ramflcdom |
| a_dg | 440 | expb_pow_hyb_ram | expb_pow_ztt_el | 0.1208 | [0.1124, 0.1292] | expb_pow_ztt_el |
| a_dg | 440 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 0.0133 | [0.0116, 0.0148] | indistinguishable |
| a_dg | 440 | expb_pow_hyb_ramfl | expb_pow_ztt_el | 0.0046 | [-0.0097, 0.0170] | indistinguishable |
| a_dg | 440 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -0.0087 | [-0.0224, 0.0036] | indistinguishable |
| a_dg | 443 | expb_pow_hyb_el | expb_pow_hyb_ram | -0.0895 | [-0.0958, -0.0837] | indistinguishable |
| a_dg | 443 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 0.0305 | [0.0180, 0.0428] | indistinguishable |
| a_dg | 443 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.0426 | [0.0304, 0.0569] | indistinguishable |
| a_dg | 443 | expb_pow_hyb_el | expb_pow_ztt_el | 0.0310 | [0.0250, 0.0365] | indistinguishable |
| a_dg | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 0.1200 | [0.1081, 0.1329] | expb_pow_hyb_ramfl |
| a_dg | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 0.1322 | [0.1198, 0.1460] | expb_pow_hyb_ramflcdom |
| a_dg | 443 | expb_pow_hyb_ram | expb_pow_ztt_el | 0.1205 | [0.1116, 0.1290] | expb_pow_ztt_el |
| a_dg | 443 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 0.0122 | [0.0106, 0.0138] | indistinguishable |
| a_dg | 443 | expb_pow_hyb_ramfl | expb_pow_ztt_el | 0.0006 | [-0.0142, 0.0136] | indistinguishable |
| a_dg | 443 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -0.0116 | [-0.0254, 0.0015] | indistinguishable |
| bb_p | 555 | expb_pow_hyb_el | expb_pow_hyb_ram | 0.2907 | [0.2828, 0.2992] | expb_pow_hyb_ram |
| bb_p | 555 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 0.3100 | [0.3019, 0.3176] | expb_pow_hyb_ramfl |
| bb_p | 555 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.2978 | [0.2870, 0.3076] | expb_pow_hyb_ramflcdom |
| bb_p | 555 | expb_pow_hyb_el | expb_pow_ztt_el | -0.1338 | [-0.1353, -0.1323] | expb_pow_hyb_el |
| bb_p | 555 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 0.0193 | [0.0171, 0.0215] | indistinguishable |
| bb_p | 555 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 0.0071 | [0.0012, 0.0130] | indistinguishable |
| bb_p | 555 | expb_pow_hyb_ram | expb_pow_ztt_el | -0.4246 | [-0.4325, -0.4165] | expb_pow_hyb_ram |
| bb_p | 555 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | -0.0121 | [-0.0170, -0.0073] | indistinguishable |
| bb_p | 555 | expb_pow_hyb_ramfl | expb_pow_ztt_el | -0.4438 | [-0.4525, -0.4351] | expb_pow_hyb_ramfl |
| bb_p | 555 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -0.4317 | [-0.4430, -0.4214] | expb_pow_hyb_ramflcdom |
| bb_p | 670 | expb_pow_hyb_el | expb_pow_hyb_ram | 0.3382 | [0.3295, 0.3468] | expb_pow_hyb_ram |
| bb_p | 670 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 0.4214 | [0.4131, 0.4299] | expb_pow_hyb_ramfl |
| bb_p | 670 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.4671 | [0.4572, 0.4779] | expb_pow_hyb_ramflcdom |
| bb_p | 670 | expb_pow_hyb_el | expb_pow_ztt_el | -0.0756 | [-0.0767, -0.0745] | indistinguishable |
| bb_p | 670 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 0.0833 | [0.0798, 0.0868] | indistinguishable |
| bb_p | 670 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 0.1290 | [0.1228, 0.1350] | expb_pow_hyb_ramflcdom |
| bb_p | 670 | expb_pow_hyb_ram | expb_pow_ztt_el | -0.4137 | [-0.4220, -0.4055] | expb_pow_hyb_ram |
| bb_p | 670 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 0.0456 | [0.0407, 0.0505] | indistinguishable |
| bb_p | 670 | expb_pow_hyb_ramfl | expb_pow_ztt_el | -0.4970 | [-0.5049, -0.4890] | expb_pow_hyb_ramfl |
| bb_p | 670 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -0.5427 | [-0.5537, -0.5314] | expb_pow_hyb_ramflcdom |

## PANGAEA-97 (in-situ noise) — `rt_tests_A_pangaea_v1`

### Fit quality, mcmc

| variant | n_attempted | frac_ok | frac_poor_fit | frac_out_of_scope | chi2_nu median | rel_misfit median |
|---|---|---|---|---|---|---|
| expb_pow_ztt_el | 97 | 0.773 | 0.206 | 0.000 | 1.66 | 0.048 |
| expb_pow_hyb_el | 97 | 0.856 | 0.124 | 0.000 | 1.45 | 0.046 |
| expb_pow_hyb_ram | 97 | 0.856 | 0.124 | 0.000 | 1.53 | 0.046 |
| expb_pow_hyb_ramfl | 97 | 0.742 | 0.237 | 0.000 | 2.10 | 0.050 |
| expb_pow_hyb_ramflcdom | 97 | 0.794 | 0.186 | 0.000 | 1.94 | 0.045 |

### Accuracy vs truth, mcmc (MAE and bias are fractional, log-space; cov68 nominal 0.68)

| variant | a(440) MAE / bias / cov68 | a_ph(440) MAE / bias / cov68 | a_dg(440) MAE / bias / cov68 | bb_p(555) MAE / bias / cov68 | bb_p(670) MAE / bias / cov68 |
|---|---|---|---|---|---|
| expb_pow_ztt_el |  /  /  (n=0) | 0.507 / 0.208 / 0.61 (n=75) | 2.864 / -0.736 / 0.36 (n=75) | 0.498 / 0.465 / 0.08 (n=75) |  |
| expb_pow_hyb_el |  /  /  (n=0) | 0.764 / -0.120 / 0.57 (n=83) | 2.130 / -0.667 / 0.55 (n=83) | 0.300 / 0.241 / 0.30 (n=82) |  |
| expb_pow_hyb_ram |  /  /  (n=0) | 1.006 / -0.281 / 0.47 (n=83) | 1.848 / -0.625 / 0.60 (n=83) | 0.238 / 0.141 / 0.49 (n=82) |  |
| expb_pow_hyb_ramfl |  /  /  (n=0) | 2.179 / -0.662 / 0.36 (n=72) | 0.361 / -0.073 / 0.74 (n=72) | 0.192 / -0.027 / 0.54 (n=72) |  |
| expb_pow_hyb_ramflcdom |  /  /  (n=0) | 3.716 / -0.758 / 0.35 (n=77) | 0.373 / -0.089 / 0.70 (n=77) | 0.414 / -0.175 / 0.42 (n=77) |  |

### Fit quality, chisq

| variant | n_attempted | frac_ok | frac_poor_fit | frac_out_of_scope | chi2_nu median | rel_misfit median |
|---|---|---|---|---|---|---|
| expb_pow_ztt_el | 97 | 0.876 | 0.103 | 0.000 | 0.82 | 0.032 |
| expb_pow_hyb_el | 97 | 0.928 | 0.052 | 0.000 | 0.44 | 0.018 |
| expb_pow_hyb_ram | 97 | 0.948 | 0.031 | 0.000 | 0.45 | 0.020 |
| expb_pow_hyb_ramfl | 97 | 0.876 | 0.103 | 0.000 | 1.26 | 0.043 |
| expb_pow_hyb_ramflcdom | 97 | 0.918 | 0.062 | 0.000 | 1.04 | 0.040 |

### Accuracy vs truth, chisq (MAE and bias are fractional, log-space; cov68 nominal 0.68)

| variant | a(440) MAE / bias / cov68 | a_ph(440) MAE / bias / cov68 | a_dg(440) MAE / bias / cov68 | bb_p(555) MAE / bias / cov68 | bb_p(670) MAE / bias / cov68 |
|---|---|---|---|---|---|
| expb_pow_ztt_el |  /  /  (n=0) | 0.594 / 0.509 / 0.85 (n=85) | 0.825 / -0.384 / 0.94 (n=85) | 0.626 / 0.594 / 0.48 (n=84) |  |
| expb_pow_hyb_el |  /  /  (n=0) | 0.467 / 0.184 / 0.81 (n=90) | 0.606 / -0.229 / 0.93 (n=90) | 0.386 / 0.313 / 0.62 (n=88) |  |
| expb_pow_hyb_ram |  /  /  (n=0) | 0.513 / 0.137 / 0.79 (n=92) | 0.593 / -0.183 / 0.93 (n=92) | 0.376 / 0.180 / 0.72 (n=90) |  |
| expb_pow_hyb_ramfl |  /  /  (n=0) | 0.572 / -0.232 / 0.93 (n=85) | 0.304 / -0.039 / 0.96 (n=85) | 0.225 / 0.037 / 0.88 (n=84) |  |
| expb_pow_hyb_ramflcdom |  /  /  (n=0) | 0.864 / -0.371 / 0.91 (n=89) | 0.313 / -0.009 / 0.96 (n=89) | 0.369 / -0.121 / 0.88 (n=88) |  |

### Model selection (delta-BIC), configured contest

| fit | model_a (more complex) | model_b | n | frac favour a | frac favour b | median dBIC |
|---|---|---|---|---|---|---|
| chisq | expb_pow_hyb_el | expb_pow_hyb_ram | 90 | 0.644 | 0.356 | -0.0 |
| chisq | expb_pow_hyb_el | expb_pow_hyb_ramfl | 85 | 0.859 | 0.141 | -1.0 |
| chisq | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 88 | 0.818 | 0.182 | -0.6 |
| chisq | expb_pow_hyb_el | expb_pow_ztt_el | 85 | 0.835 | 0.165 | -0.5 |
| chisq | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 85 | 0.871 | 0.129 | -1.0 |
| chisq | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 89 | 0.809 | 0.191 | -0.7 |
| chisq | expb_pow_hyb_ram | expb_pow_ztt_el | 85 | 0.824 | 0.176 | -0.5 |
| chisq | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 85 | 0.118 | 0.882 | 0.4 |
| chisq | expb_pow_hyb_ramfl | expb_pow_ztt_el | 83 | 0.217 | 0.783 | 0.4 |
| chisq | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | 84 | 0.405 | 0.595 | 0.1 |
| mcmc | expb_pow_hyb_el | expb_pow_hyb_ram | 82 | 0.646 | 0.354 | -0.1 |
| mcmc | expb_pow_hyb_el | expb_pow_hyb_ramfl | 71 | 0.718 | 0.282 | -1.4 |
| mcmc | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 72 | 0.681 | 0.319 | -1.1 |
| mcmc | expb_pow_hyb_el | expb_pow_ztt_el | 75 | 0.760 | 0.240 | -0.7 |
| mcmc | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 71 | 0.690 | 0.310 | -1.2 |
| mcmc | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 72 | 0.694 | 0.306 | -1.1 |
| mcmc | expb_pow_hyb_ram | expb_pow_ztt_el | 74 | 0.730 | 0.270 | -0.6 |
| mcmc | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | 72 | 0.125 | 0.875 | 0.4 |
| mcmc | expb_pow_hyb_ramfl | expb_pow_ztt_el | 68 | 0.294 | 0.706 | 0.8 |
| mcmc | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | 68 | 0.397 | 0.603 | 0.4 |

### Head-to-head, mcmc (paired bootstrap, 10% equivalence floor)

| component | ref_wave | model_a | model_b | delta MAE (a - b) | 95% CI | verdict |
|---|---|---|---|---|---|---|
| a_ph | 440 | expb_pow_hyb_el | expb_pow_hyb_ram | -0.1856 | [-0.2888, -0.0984] | expb_pow_hyb_el |
| a_ph | 440 | expb_pow_hyb_el | expb_pow_hyb_ramfl | -1.2903 | [-2.0938, -0.7021] | expb_pow_hyb_el |
| a_ph | 440 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | -2.0639 | [-3.3904, -1.1568] | expb_pow_hyb_el |
| a_ph | 440 | expb_pow_hyb_el | expb_pow_ztt_el | 0.1719 | [0.0319, 0.3135] | expb_pow_ztt_el |
| a_ph | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | -1.2553 | [-1.9572, -0.6522] | expb_pow_hyb_ram |
| a_ph | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | -2.0544 | [-3.3299, -1.1299] | expb_pow_hyb_ram |
| a_ph | 440 | expb_pow_hyb_ram | expb_pow_ztt_el | 0.3186 | [0.1288, 0.5342] | expb_pow_ztt_el |
| a_ph | 440 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | -0.6048 | [-1.0305, -0.2989] | expb_pow_hyb_ramfl |
| a_ph | 440 | expb_pow_hyb_ramfl | expb_pow_ztt_el | 1.3107 | [0.7151, 2.0805] | expb_pow_ztt_el |
| a_ph | 440 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | 1.8911 | [1.0498, 3.1069] | expb_pow_ztt_el |
| a_ph | 443 | expb_pow_hyb_el | expb_pow_hyb_ram | -0.1856 | [-0.2969, -0.1015] | expb_pow_hyb_el |
| a_ph | 443 | expb_pow_hyb_el | expb_pow_hyb_ramfl | -1.2903 | [-2.1307, -0.7244] | expb_pow_hyb_el |
| a_ph | 443 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | -2.0639 | [-3.2061, -1.1039] | expb_pow_hyb_el |
| a_ph | 443 | expb_pow_hyb_el | expb_pow_ztt_el | 0.1719 | [0.0428, 0.3212] | expb_pow_ztt_el |
| a_ph | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | -1.2553 | [-1.9896, -0.6587] | expb_pow_hyb_ram |
| a_ph | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | -2.0544 | [-3.4856, -1.1274] | expb_pow_hyb_ram |
| a_ph | 443 | expb_pow_hyb_ram | expb_pow_ztt_el | 0.3186 | [0.1306, 0.5474] | expb_pow_ztt_el |
| a_ph | 443 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | -0.6048 | [-1.0695, -0.2928] | expb_pow_hyb_ramfl |
| a_ph | 443 | expb_pow_hyb_ramfl | expb_pow_ztt_el | 1.3107 | [0.7183, 2.1159] | expb_pow_ztt_el |
| a_ph | 443 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | 1.8911 | [1.0108, 3.0372] | expb_pow_ztt_el |
| a_dg | 440 | expb_pow_hyb_el | expb_pow_hyb_ram | 0.1724 | [0.0782, 0.3182] | expb_pow_hyb_ram |
| a_dg | 440 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 2.2404 | [1.0540, 3.9505] | expb_pow_hyb_ramfl |
| a_dg | 440 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 2.1821 | [1.0797, 4.2080] | expb_pow_hyb_ramflcdom |
| a_dg | 440 | expb_pow_hyb_el | expb_pow_ztt_el | -0.5273 | [-0.8520, -0.3382] | expb_pow_hyb_el |
| a_dg | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 1.8824 | [0.8473, 3.7003] | expb_pow_hyb_ramfl |
| a_dg | 440 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 1.8325 | [0.8375, 3.5580] | expb_pow_hyb_ramflcdom |
| a_dg | 440 | expb_pow_hyb_ram | expb_pow_ztt_el | -0.6850 | [-1.0681, -0.4376] | expb_pow_hyb_ram |
| a_dg | 440 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | -0.0147 | [-0.0327, 0.0033] | indistinguishable |
| a_dg | 440 | expb_pow_hyb_ramfl | expb_pow_ztt_el | -2.9129 | [-5.3509, -1.5067] | expb_pow_hyb_ramfl |
| a_dg | 440 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -2.8979 | [-5.3621, -1.4931] | expb_pow_hyb_ramflcdom |
| a_dg | 443 | expb_pow_hyb_el | expb_pow_hyb_ram | 0.1724 | [0.0847, 0.3132] | expb_pow_hyb_ram |
| a_dg | 443 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 2.2404 | [1.0651, 4.1745] | expb_pow_hyb_ramfl |
| a_dg | 443 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 2.1821 | [1.0748, 4.2598] | expb_pow_hyb_ramflcdom |
| a_dg | 443 | expb_pow_hyb_el | expb_pow_ztt_el | -0.5273 | [-0.8525, -0.3338] | expb_pow_hyb_el |
| a_dg | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 1.8824 | [0.8168, 3.5999] | expb_pow_hyb_ramfl |
| a_dg | 443 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 1.8325 | [0.8672, 3.5623] | expb_pow_hyb_ramflcdom |
| a_dg | 443 | expb_pow_hyb_ram | expb_pow_ztt_el | -0.6850 | [-1.0732, -0.4467] | expb_pow_hyb_ram |
| a_dg | 443 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | -0.0147 | [-0.0339, 0.0025] | indistinguishable |
| a_dg | 443 | expb_pow_hyb_ramfl | expb_pow_ztt_el | -2.9129 | [-5.3103, -1.4667] | expb_pow_hyb_ramfl |
| a_dg | 443 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -2.8979 | [-5.1831, -1.4840] | expb_pow_hyb_ramflcdom |
| bb_p | 555 | expb_pow_hyb_el | expb_pow_hyb_ram | 0.0484 | [0.0280, 0.0703] | indistinguishable |
| bb_p | 555 | expb_pow_hyb_el | expb_pow_hyb_ramfl | 0.1337 | [0.0693, 0.1968] | expb_pow_hyb_ramfl |
| bb_p | 555 | expb_pow_hyb_el | expb_pow_hyb_ramflcdom | 0.1006 | [0.0314, 0.1740] | expb_pow_hyb_ramflcdom |
| bb_p | 555 | expb_pow_hyb_el | expb_pow_ztt_el | -0.1817 | [-0.2091, -0.1521] | expb_pow_hyb_el |
| bb_p | 555 | expb_pow_hyb_ram | expb_pow_hyb_ramfl | 0.0689 | [0.0179, 0.1282] | underpowered |
| bb_p | 555 | expb_pow_hyb_ram | expb_pow_hyb_ramflcdom | 0.0379 | [-0.0244, 0.1102] | underpowered |
| bb_p | 555 | expb_pow_hyb_ram | expb_pow_ztt_el | -0.2435 | [-0.2813, -0.1999] | expb_pow_hyb_ram |
| bb_p | 555 | expb_pow_hyb_ramfl | expb_pow_hyb_ramflcdom | -0.0265 | [-0.0466, -0.0077] | indistinguishable |
| bb_p | 555 | expb_pow_hyb_ramfl | expb_pow_ztt_el | -0.3118 | [-0.3928, -0.2242] | expb_pow_hyb_ramfl |
| bb_p | 555 | expb_pow_hyb_ramflcdom | expb_pow_ztt_el | -0.2913 | [-0.3825, -0.2067] | expb_pow_hyb_ramflcdom |
