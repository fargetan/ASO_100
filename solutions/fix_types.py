dta.l_ipn = dta.l_ipn.astype('category')
dta.r_asn = dta.r_asn.astype('category')
dta.describe(include='all')