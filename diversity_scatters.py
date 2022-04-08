import pandas as pd

df = pd.read_csv('headcount_data.csv')

df = df[df.firm_auto_namenid != 'test']
df = df.fillna(0)

df['total_hc1'] = df['hc1_part_male_hisp'] + df['hc1_part_male_black'] + df['hc1_part_male_asian'] + df['hc1_part_male_white'] + df['hc1_part_male_pi'] + df['hc1_part_male_nata'] + df['hc1_part_male_tomr'] + df['hc1_part_male_norace'] + df['hc1_part_fem_hisp'] + df['hc1_part_fem_black'] + df['hc1_part_fem_asian'] + df['hc1_part_fem_white'] + df['hc1_part_fem_pi'] + df['hc1_part_fem_nata'] + df['hc1_part_fem_tomr'] + df['hc1_part_fem_norace'] + df['hc1_part_nb_hisp'] + df['hc1_part_nb_black'] + df['hc1_part_nb_asian'] + df['hc1_part_nb_white'] +df['hc1_part_nb_pi'] + df['hc1_part_nb_nata'] +df['hc1_part_nb_tomr'] + df['hc1_part_nb_norace'] +df['hc1_part_nogen_hisp'] + df['hc1_part_nogen_black'] +df['hc1_part_nogen_asian'] + df['hc1_part_nogen_white'] +df['hc1_part_nogen_pi'] + df['hc1_part_nogen_nata'] + df['hc1_part_nogen_tomr'] + df['hc1_part_nogen_norace'] +df['hc1_eq_male_hisp'] + df['hc1_eq_male_black'] +df['hc1_eq_male_asian'] + df['hc1_eq_male_white'] +df['hc1_eq_male_pi'] + df['hc1_eq_male_nata'] + df['hc1_eq_male_tomr'] + df['hc1_eq_male_norace'] +df['hc1_eq_fem_hisp'] + df['hc1_eq_fem_black'] +df['hc1_eq_fem_asian'] + df['hc1_eq_fem_white'] +df['hc1_eq_fem_pi'] + df['hc1_eq_fem_nata'] +df['hc1_eq_fem_tomr'] + df['hc1_eq_fem_norace'] +df['hc1_eq_nb_hisp'] + df['hc1_eq_nb_black'] +df['hc1_eq_nb_asian'] + df['hc1_eq_nb_white'] +df['hc1_eq_nb_pi'] + df['hc1_eq_nb_nata'] +df['hc1_eq_nb_tomr'] + df['hc1_eq_nb_norace'] +df['hc1_eq_nogen_hisp'] +df['hc1_eq_nogen_black'] +df['hc1_eq_nogen_asian'] + df['hc1_eq_nogen_white'] +df['hc1_eq_nogen_pi'] + df['hc1_eq_nogen_nata'] +df['hc1_eq_nogen_tomr'] + df['hc1_eq_nogen_norace'] + df['hc1_noneq_male_hisp'] + df['hc1_noneq_male_black'] + df['hc1_noneq_male_asian'] + df['hc1_noneq_male_white'] +df['hc1_noneq_male_pi'] + df['hc1_noneq_male_nata'] + df['hc1_noneq_male_tomr'] + df['hc1_noneq_male_norace'] +df['hc1_noneq_fem_hisp'] + df['hc1_noneq_fem_black'] + df['hc1_noneq_fem_asian'] +df['hc1_noneq_fem_white'] +df['hc1_noneq_fem_pi'] + df['hc1_noneq_fem_nata'] +df['hc1_noneq_fem_tomr'] + df['hc1_noneq_fem_norace'] + df['hc1_noneq_nb_hisp'] + df['hc1_noneq_nb_black'] +df['hc1_noneq_nb_asian'] + df['hc1_noneq_nb_white'] +df['hc1_noneq_nb_pi'] + df['hc1_noneq_nb_nata'] + df['hc1_noneq_nb_tomr'] + df['hc1_noneq_nb_norace'] +df['hc1_noneq_nogen_hisp'] + df['hc1_noneq_nogen_black'] +df['hc1_noneq_nogen_asian'] + df['hc1_noneq_nogen_white'] +df['hc1_noneq_nogen_pi'] +df['hc1_noneq_nogen_nata'] +df['hc1_noneq_nogen_tomr'] + df['hc1_noneq_nogen_norace'] + df['hc1_other_male_hisp'] + df['hc1_other_male_black'] + df['hc1_other_male_asian'] + df['hc1_other_male_white'] + df['hc1_other_male_pi'] + df['hc1_other_male_nata'] + df['hc1_other_male_tomr'] + df['hc1_other_male_norace'] + df['hc1_other_fem_hisp'] + df['hc1_other_fem_black'] + df['hc1_other_fem_asian'] + df['hc1_other_fem_white'] + df['hc1_other_fem_pi'] + df['hc1_other_fem_nata'] +df['hc1_other_fem_tomr'] + df['hc1_other_fem_norace'] + df['hc1_other_nb_hisp'] + df['hc1_other_nb_black'] + df['hc1_other_nb_asian'] + df['hc1_other_nb_white'] + df['hc1_other_nb_pi'] + df['hc1_other_nb_nata'] + df['hc1_other_nb_tomr'] + df['hc1_other_nb_norace'] + df['hc1_other_nogen_hisp'] + df['hc1_other_nogen_black'] +df['hc1_other_nogen_asian'] + df['hc1_other_nogen_white'] +df['hc1_other_nogen_pi'] + df['hc1_other_nogen_nata'] +df['hc1_other_nogen_tomr'] + df['hc1_other_nogen_norace']+ df['hc1_assoc_male_hisp'] + df['hc1_assoc_male_black'] + df['hc1_assoc_male_asian'] + df['hc1_assoc_male_white'] +df['hc1_assoc_male_pi'] + df['hc1_assoc_male_nata'] + df['hc1_assoc_male_tomr'] + df['hc1_assoc_male_norace'] + df['hc1_assoc_fem_hisp'] + df['hc1_assoc_fem_black'] + df['hc1_assoc_fem_asian'] + df['hc1_assoc_fem_white'] + df['hc1_assoc_fem_pi'] + df['hc1_assoc_fem_nata'] + df['hc1_assoc_fem_tomr'] + df['hc1_assoc_fem_norace'] + df['hc1_assoc_nb_hisp'] + df['hc1_assoc_nb_black'] +df['hc1_assoc_nb_asian'] + df['hc1_assoc_nb_white'] + df['hc1_assoc_nb_pi'] + df['hc1_assoc_nb_nata'] +df['hc1_assoc_nb_tomr'] + df['hc1_assoc_nb_norace'] + df['hc1_assoc_nogen_hisp'] + df['hc1_assoc_nogen_black'] + df['hc1_assoc_nogen_asian'] + df['hc1_assoc_nogen_white'] +df['hc1_assoc_nogen_pi'] + df['hc1_assoc_nogen_nata'] + df['hc1_assoc_nogen_tomr'] + df['hc1_assoc_nogen_norace']

df['total_diversity_hc1'] = df['hc1_part_male_hisp'] + df['hc1_part_male_black'] + df['hc1_part_male_asian'] + df['hc1_part_male_pi'] + df['hc1_part_male_nata'] + df['hc1_part_male_tomr'] + df['hc1_part_fem_hisp'] + df['hc1_part_fem_black'] + df['hc1_part_fem_asian'] + df['hc1_part_fem_pi'] + df['hc1_part_fem_nata'] + df['hc1_part_fem_tomr'] + df['hc1_part_nb_hisp'] + df['hc1_part_nb_black'] + df['hc1_part_nb_asian'] + df['hc1_part_nb_pi'] + df['hc1_part_nb_nata'] +df['hc1_part_nb_tomr'] +df['hc1_part_nogen_hisp'] + df['hc1_part_nogen_black'] +df['hc1_part_nogen_asian'] + df['hc1_part_nogen_pi'] + df['hc1_part_nogen_nata'] + df['hc1_part_nogen_tomr'] + df['hc1_eq_male_hisp'] + df['hc1_eq_male_black'] + df['hc1_eq_male_asian'] + df['hc1_eq_male_pi'] + df['hc1_eq_male_nata'] + df['hc1_eq_male_tomr'] + df['hc1_eq_fem_hisp'] + df['hc1_eq_fem_black'] + df['hc1_eq_fem_asian'] + df['hc1_eq_fem_pi'] + df['hc1_eq_fem_nata'] + df['hc1_eq_fem_tomr'] + df['hc1_eq_nb_hisp'] +df['hc1_eq_nb_black'] + df['hc1_eq_nb_asian'] + df['hc1_eq_nb_pi'] + df['hc1_eq_nb_nata'] + df['hc1_eq_nb_tomr'] + df['hc1_eq_nogen_hisp'] + df['hc1_eq_nogen_black'] + df['hc1_eq_nogen_asian'] + df['hc1_eq_nogen_pi'] + df['hc1_eq_nogen_nata'] + df['hc1_eq_nogen_tomr'] + df['hc1_noneq_male_hisp'] + df['hc1_noneq_male_black'] + df['hc1_noneq_male_asian'] + df['hc1_noneq_male_pi'] + df['hc1_noneq_male_nata'] + df['hc1_noneq_male_tomr'] + df['hc1_noneq_fem_hisp'] + df['hc1_noneq_fem_black'] +df['hc1_noneq_fem_asian'] + df['hc1_noneq_fem_pi'] + df['hc1_noneq_fem_nata'] +df['hc1_noneq_fem_tomr'] + df['hc1_noneq_nb_hisp'] + df['hc1_noneq_nb_black'] + df['hc1_noneq_nb_asian'] + df['hc1_noneq_nb_pi'] + df['hc1_noneq_nb_nata'] + df['hc1_noneq_nb_tomr'] + df['hc1_noneq_nogen_hisp'] + df['hc1_noneq_nogen_black'] +df['hc1_noneq_nogen_asian'] + df['hc1_noneq_nogen_pi'] + df['hc1_noneq_nogen_nata'] + df['hc1_noneq_nogen_tomr'] + df['hc1_other_male_hisp'] + df['hc1_other_male_black'] +df['hc1_other_male_asian'] + df['hc1_other_male_pi'] + df['hc1_other_male_nata'] + df['hc1_other_male_tomr'] + df['hc1_other_fem_hisp'] + df['hc1_other_fem_black'] + df['hc1_other_fem_asian'] + df['hc1_other_fem_pi'] + df['hc1_other_fem_nata'] + df['hc1_other_fem_tomr'] + df['hc1_other_nb_hisp'] + df['hc1_other_nb_black'] + df['hc1_other_nb_asian'] + df['hc1_other_nb_pi'] + df['hc1_other_nb_nata'] + df['hc1_other_nb_tomr'] + df['hc1_other_nogen_hisp'] + df['hc1_other_nogen_black'] +df['hc1_other_nogen_asian'] + df['hc1_other_nogen_pi'] + df['hc1_other_nogen_nata'] + df['hc1_other_nogen_tomr'] + df['hc1_assoc_male_hisp'] + df['hc1_assoc_male_black'] + df['hc1_assoc_male_asian'] + df['hc1_assoc_male_pi'] + df['hc1_assoc_male_nata'] + df['hc1_assoc_male_tomr'] + df['hc1_assoc_fem_hisp'] + df['hc1_assoc_fem_black'] + df['hc1_assoc_fem_asian'] + df['hc1_assoc_fem_pi'] + df['hc1_assoc_fem_nata'] + df['hc1_assoc_fem_tomr'] + df['hc1_assoc_nb_hisp'] + df['hc1_assoc_nb_black'] +df['hc1_assoc_nb_asian'] + df['hc1_assoc_nb_pi'] + df['hc1_assoc_nb_nata'] +df['hc1_assoc_nb_tomr'] + df['hc1_assoc_nogen_hisp'] + df['hc1_assoc_nogen_black'] + df['hc1_assoc_nogen_asian'] + df['hc1_assoc_nogen_pi'] + df['hc1_assoc_nogen_nata'] + df['hc1_assoc_nogen_tomr']

df['diversity_proportion'] = df['total_diversity_hc1'] / df['total_hc1']

df['diversity_hc1_partners'] = df['hc1_part_male_hisp'] + df['hc1_part_male_black'] + df['hc1_part_male_asian'] + df['hc1_part_male_pi'] + df['hc1_part_male_nata'] + df['hc1_part_male_tomr'] + df['hc1_part_fem_hisp'] + df['hc1_part_fem_black'] + df['hc1_part_fem_asian'] + df['hc1_part_fem_pi'] + df['hc1_part_fem_nata'] + df['hc1_part_fem_tomr']
df['diversity_hc1_partners_proportion'] = df['diversity_hc1_partners'] / df['total_hc1']

df['diversity_hc1_equity_partners'] = df['hc1_eq_male_hisp'] + df['hc1_eq_male_black'] + df['hc1_eq_male_asian'] + df['hc1_eq_male_pi'] + df['hc1_eq_male_nata'] + df['hc1_eq_male_tomr'] + df['hc1_eq_fem_hisp'] + df['hc1_eq_fem_black'] + df['hc1_eq_fem_asian'] + df['hc1_eq_fem_pi'] + df['hc1_eq_fem_nata'] + df['hc1_eq_fem_tomr'] + df['hc1_eq_nb_hisp'] + df['hc1_eq_nb_black'] + df['hc1_eq_nb_asian'] + df['hc1_eq_nb_pi'] + df['hc1_eq_nb_nata'] + df['hc1_eq_nb_tomr'] + df['hc1_eq_nogen_hisp'] +df['hc1_eq_nogen_black'] + df['hc1_eq_nogen_asian'] + df['hc1_eq_nogen_pi'] + df['hc1_eq_nogen_nata'] + df['hc1_eq_nogen_tomr']

df['diversity_hc1_equity_partners_proportion'] = df['diversity_hc1_equity_partners'] / df['total_hc1']

df['diversity_hc1_nonequity_partners'] = df['hc1_noneq_male_hisp'] + df['hc1_noneq_male_black'] + df['hc1_noneq_male_asian'] + df['hc1_noneq_male_pi'] + df['hc1_noneq_male_nata'] + df['hc1_noneq_male_tomr'] + df['hc1_noneq_fem_hisp'] + df['hc1_noneq_fem_black'] + df['hc1_noneq_fem_asian'] + df['hc1_noneq_fem_pi'] + df['hc1_noneq_fem_nata'] + df['hc1_noneq_fem_tomr'] + df['hc1_noneq_nb_hisp'] + df['hc1_noneq_nb_black'] + df['hc1_noneq_nb_asian'] + df['hc1_noneq_nb_pi'] + df['hc1_noneq_nb_nata']+ df['hc1_noneq_nb_tomr'] + df['hc1_noneq_nogen_hisp'] + df['hc1_noneq_nogen_black'] + df['hc1_noneq_nogen_asian'] + df['hc1_noneq_nogen_pi'] + df['hc1_noneq_nogen_nata'] + df['hc1_noneq_nogen_tomr']

df['diversity_hc1_nonequity_partners_proportion'] = df['diversity_hc1_nonequity_partners'] / df['total_hc1']

df['diversity_hc1_associates'] = df['hc1_assoc_male_hisp'] + df['hc1_assoc_male_black'] + df['hc1_assoc_male_asian'] + df['hc1_assoc_male_pi'] + df['hc1_assoc_male_nata'] + df['hc1_assoc_male_tomr'] + df['hc1_assoc_fem_hisp'] + df['hc1_assoc_fem_black'] + df['hc1_assoc_fem_asian'] + df['hc1_assoc_fem_pi'] + df['hc1_assoc_fem_nata'] + df['hc1_assoc_fem_tomr'] + df['hc1_assoc_nb_hisp'] + df['hc1_assoc_nb_black'] + df['hc1_assoc_nb_asian'] + df['hc1_assoc_nb_pi'] + df['hc1_assoc_nb_nata'] +df['hc1_assoc_nb_tomr'] + df['hc1_assoc_nogen_hisp'] + df['hc1_assoc_nogen_black'] + df['hc1_assoc_nogen_asian'] + df['hc1_assoc_nogen_pi'] + df['hc1_assoc_nogen_nata'] + df['hc1_assoc_nogen_tomr']

df['diversity_hc1_associates_proportion'] = df['diversity_hc1_associates'] / df['total_hc1']

df['diversity_hc1_other'] = df['hc1_other_male_hisp'] + df['hc1_other_male_black'] + df['hc1_other_male_asian'] + df['hc1_other_male_pi'] + df['hc1_other_male_nata'] + df['hc1_other_male_tomr'] + df['hc1_other_fem_hisp'] + df['hc1_other_fem_black'] + df['hc1_other_fem_asian'] + df['hc1_other_fem_pi'] + df['hc1_other_fem_nata'] + df['hc1_other_fem_tomr'] + df['hc1_other_nb_hisp'] + df['hc1_other_nb_black'] + df['hc1_other_nb_asian'] + df['hc1_other_nb_pi'] + df['hc1_other_nb_nata'] +df['hc1_other_nb_tomr'] + df['hc1_other_nogen_hisp'] + df['hc1_other_nogen_black'] + df['hc1_other_nogen_asian'] + df['hc1_other_nogen_pi'] + df['hc1_other_nogen_nata'] + df['hc1_other_nogen_tomr']

df['diversity_hc1_other_proportion'] = df['diversity_hc1_other'] / df['total_hc1']

df['women'] = df['hc1_part_fem_hisp'] + df['hc1_part_fem_white'] + df['hc1_part_fem_black'] + df['hc1_part_fem_asian'] + df['hc1_part_fem_pi'] + df['hc1_part_fem_nata'] + df['hc1_part_fem_tomr'] + df['hc1_eq_fem_hisp'] + df['hc1_eq_fem_white'] + df['hc1_eq_fem_black'] + df['hc1_eq_fem_asian'] + df['hc1_eq_fem_pi'] + df['hc1_eq_fem_nata'] + df['hc1_eq_fem_tomr'] + df['hc1_noneq_fem_hisp'] + df['hc1_noneq_fem_white'] + df['hc1_noneq_fem_black'] + df['hc1_noneq_fem_asian'] + df['hc1_noneq_fem_pi'] + df['hc1_noneq_fem_nata'] + df['hc1_noneq_fem_tomr'] + df['hc1_other_fem_hisp'] + df['hc1_other_fem_white'] + df['hc1_other_fem_black'] + df['hc1_other_fem_asian'] + df['hc1_other_fem_pi'] + df['hc1_other_fem_nata'] + df['hc1_other_fem_tomr'] + df['hc1_assoc_fem_hisp'] + df['hc1_assoc_fem_white'] + df['hc1_assoc_fem_black'] + df['hc1_assoc_fem_asian'] + df['hc1_assoc_fem_pi'] + df['hc1_assoc_fem_nata'] + df['hc1_assoc_fem_tomr']

df['women_proportion'] = df['women'] / df['total_hc1']

df['women_partner'] = df['hc1_part_fem_hisp'] + df['hc1_part_fem_black'] + df['hc1_part_fem_asian'] + df['hc1_part_fem_white'] + df['hc1_part_fem_pi'] + df['hc1_part_fem_nata'] + df['hc1_part_fem_tomr'] + df['hc1_part_fem_norace']

df['women_partner_proportion'] = df['women_partner'] / df['total_hc1']

df['women_equity'] = df['hc1_eq_fem_hisp'] + df['hc1_eq_fem_black'] + df['hc1_eq_fem_asian'] + df['hc1_eq_fem_white'] + df['hc1_eq_fem_pi'] + df['hc1_eq_fem_nata'] + df['hc1_eq_fem_tomr'] + df['hc1_eq_fem_norace']

df['women_equity_proportion'] = df['women_equity'] / df['total_hc1']

df['women_nonequity'] = df['hc1_noneq_fem_hisp'] + df['hc1_noneq_fem_black'] + df['hc1_noneq_fem_asian'] + df['hc1_noneq_fem_white'] + df['hc1_noneq_fem_pi'] + df['hc1_noneq_fem_nata'] + df['hc1_noneq_fem_tomr'] + df['hc1_noneq_fem_norace']

df['women_nonequity_proportion'] = df['women_nonequity'] / df['total_hc1']

df['women_associate'] = df['hc1_assoc_fem_hisp'] + df['hc1_assoc_fem_black'] + df['hc1_assoc_fem_asian'] + df['hc1_assoc_fem_white'] + df['hc1_assoc_fem_pi'] + df['hc1_assoc_fem_nata'] + df['hc1_assoc_fem_tomr'] + df['hc1_assoc_fem_norace']

df['women_associate_proportion'] = df['women_associate'] / df['total_hc1']

df['women_other'] = df['hc1_other_fem_hisp'] + df['hc1_other_fem_black'] + df['hc1_other_fem_asian'] + df['hc1_other_fem_white'] + df['hc1_other_fem_pi'] + df['hc1_other_fem_nata'] + df['hc1_other_fem_tomr'] + df['hc1_other_fem_norace']

df['women_other_proportion'] = df['women_other'] / df['total_hc1']

df['total_lgbt'] = df['hc2_part_male'] + df['hc2_part_fem'] + df['hc2_part_nb'] + df['hc2_part_nogen'] +  df['hc2_eq_male'] + df['hc2_eq_fem'] + df['hc2_eq_nb'] + df['hc2_eq_nogen'] + df['hc2_noneq_male'] + df['hc2_noneq_fem'] + df['hc2_noneq_nb'] + df['hc2_noneq_nogen'] + df['hc2_other_male'] + df['hc2_other_fem'] + df['hc2_other_nb'] + df['hc2_other_nogen'] + df['hc2_assoc_male'] + df['hc2_assoc_fem'] + df['hc2_assoc_nb'] + df['hc2_assoc_nogen']
df['lgbt_proportion'] = df['total_lgbt'] / df['total_hc1']

df['lgbt_partner'] = df['hc2_part_male'] + df['hc2_part_fem'] + df['hc2_part_nb'] + df['hc2_part_nogen']
df['lgbt_partner_proportion'] = df['lgbt_partner'] / df['total_hc1']

df['lgbt_equity_partner'] = df['hc2_eq_male'] + df['hc2_eq_fem'] + df['hc2_eq_nb'] + df['hc2_eq_nogen']
df['lgtb_equity_proportion'] = df['lgbt_equity_partner'] / df['total_hc1']

df['lgbt_nonequity_partner'] = df['hc2_noneq_male'] + df['hc2_noneq_fem'] + df['hc2_noneq_nb'] + df['hc2_noneq_nogen']
df['lgbt_nonequity_partner_proportion'] = df['lgbt_nonequity_partner'] / df['total_hc1']

df['lgbt_other'] = df['hc2_other_male'] + df['hc2_other_fem'] + df['hc2_other_nb'] + df['hc2_other_nogen']
df['lgbt_other_proportion'] = df['lgbt_other'] / df['total_hc1']

df['lgbt_associate'] = df['hc2_assoc_male'] + df['hc2_assoc_fem'] + df['hc2_assoc_nb'] + df['hc2_assoc_nogen']
df['lgbt_associate_proportion'] = df['lgbt_associate'] / df['total_hc1']

df['total_disabeled'] = df['hc3_part_male'] + df['hc3_part_fem'] + df['hc3_part_nb'] + df['hc3_part_nogen'] +df['hc3_eq_male'] +df['hc3_eq_fem'] +df['hc3_eq_nb'] +df['hc3_eq_nogen'] +df['hc3_noneq_male'] +df['hc3_noneq_fem'] +df['hc3_noneq_nb'] +df['hc3_noneq_nogen'] +df['hc3_other_male'] +df['hc3_other_fem'] +df['hc3_other_nb'] +df['hc3_other_nogen']
df['disabeled_proportion'] = df['total_disabeled'] / df['total_hc1']

df['disabled_partners'] = df['hc3_part_male'] + df['hc3_part_fem'] + df['hc3_part_nb'] + df['hc3_part_nogen']
df['disabled_partners_proportion'] = df['disabled_partners'] / df['total_hc1']

df['disabled_equity_partners'] = df['hc3_eq_male'] + df['hc3_eq_fem'] + df['hc3_eq_nb'] + df['hc3_eq_nogen']
df['disabled_equity_partners_proportion'] = df['disabled_equity_partners'] / df['total_hc1']

df['disabled_nonequity_partners'] = df['hc3_noneq_male'] + df['hc3_noneq_fem'] + df['hc3_noneq_nb'] + df['hc3_noneq_nogen']
df['disabled_nonequity_partners_proportion'] = df['disabled_nonequity_partners'] / df['total_hc1']

df['disabled_other'] = df['hc3_other_male'] + df['hc3_other_fem'] + df['hc3_other_nb'] + df['hc3_other_nogen']
df['disabled_other_proportion'] = df['disabled_other'] / df['total_hc1']

df['disabled_associate'] = df['hc3_assoc_male'] + df['hc3_assoc_fem'] + df['hc3_assoc_nb'] + df['hc3_assoc_nogen']
df['disabled_associate_proportion'] = df['disabled_associate'] / df['total_hc1']

df.to_csv('total_hc_diversity.csv')
df = pd.read_csv('total_hc_diversity.csv')

df['hispanic'] = df['hc1_part_male_hisp'] + df['hc1_part_fem_hisp'] + df['hc1_eq_male_hisp'] + df['hc1_eq_fem_hisp'] + df['hc1_eq_nb_hisp'] + df['hc1_eq_nogen_hisp'] + df['hc1_noneq_male_hisp'] + df['hc1_noneq_fem_hisp'] + df['hc1_noneq_nb_hisp'] + df['hc1_noneq_nogen_hisp'] + df['hc1_assoc_male_hisp'] + df['hc1_assoc_fem_hisp'] + df['hc1_assoc_nb_hisp'] + df['hc1_assoc_nogen_hisp'] + df['hc1_other_male_hisp'] + df['hc1_other_fem_hisp'] + df['hc1_other_nb_hisp'] + df['hc1_other_nogen_hisp']

df['hispanic_proportion'] = df['hispanic'] / df['total_hc1']

df['hispanic_partner'] = df['hc1_part_male_hisp'] + df['hc1_part_fem_hisp']

df['hispanic_partner_proportion'] = df['hispanic_partner'] / df['total_hc1']

df['hispanic_equity'] = df['hc1_eq_male_hisp'] + df['hc1_eq_fem_hisp'] + df['hc1_eq_nb_hisp'] + df['hc1_eq_nogen_hisp']

df['hispanic_equity_proportion'] = df['hispanic_equity'] / df['total_hc1']

df['hispanic_nonequity'] = df['hc1_noneq_male_hisp'] + df['hc1_noneq_fem_hisp'] + df['hc1_noneq_nb_hisp'] + df['hc1_noneq_nogen_hisp']

df['hispanic_nonequity_proportion'] = df['hispanic_nonequity'] / df['total_hc1']

df['hispanic_other'] = df['hc1_other_male_hisp'] + df['hc1_other_fem_hisp'] + df['hc1_other_nb_hisp'] + df['hc1_other_nogen_hisp']

df['hispanic_other_proportion'] = df['hispanic_other'] / df['total_hc1']

df['hispanic_associate'] = df['hc1_assoc_male_hisp'] + df['hc1_assoc_fem_hisp'] + df['hc1_assoc_nb_hisp'] + df['hc1_assoc_nogen_hisp']

df['hispanic_associate_proportion'] = df['hispanic_associate'] / df['total_hc1']

df['hispanic_female'] = df['hc1_part_fem_hisp'] + df['hc1_eq_fem_hisp'] + df['hc1_noneq_fem_hisp'] + df['hc1_assoc_fem_hisp'] + df['hc1_other_fem_hisp']

df['hispanice_female_proportion'] = df['hispanic_female'] / df['total_hc1']

df['hispanic_female_partner'] = df['hc1_part_fem_hisp']

df['hispanic_female_partner_proportion'] = df['hispanic_female_partner'] / df['total_hc1']

df['hispanic_female_equity'] = df['hc1_eq_fem_hisp']

df['hispanic_female_equity_proportion'] = df['hispanic_female_equity'] / df['total_hc1']

df['hispanic_female_nonequity'] = df['hc1_noneq_fem_hisp']

df['hispanic_female_nonequity_proportion'] = df['hispanic_female_nonequity'] / df['total_hc1']

df['hispanic_female_other'] = df['hc1_other_fem_hisp']

df['hispanic_female_other_proportion'] = df['hispanic_female_other'] / df['total_hc1']

df['hispanic_female_associate'] = df['hc1_assoc_fem_hisp']

df['hispanic_female_associate_proportion'] = df['hispanic_female_associate'] / df['total_hc1']

df['black'] = df['hc1_part_male_black'] + df['hc1_part_fem_black'] + df['hc1_eq_male_black'] + df['hc1_eq_fem_black'] + df['hc1_eq_nb_black'] + df['hc1_eq_nogen_black'] + df['hc1_noneq_male_black'] + df['hc1_noneq_fem_black'] + df['hc1_noneq_nb_black'] + df['hc1_noneq_nogen_black'] + df['hc1_assoc_male_black'] + df['hc1_assoc_fem_black'] + df['hc1_assoc_nb_black'] + df['hc1_assoc_nogen_black'] + df['hc1_other_male_black'] + df['hc1_other_fem_black'] + df['hc1_other_nb_black'] + df['hc1_other_nogen_black']

df['black_proportion'] = df['black'] / df['total_hc1']

df['black_partner'] = df['hc1_part_male_black'] + df['hc1_part_fem_black']

df['black_partner_proportion'] = df['black_partner'] / df['total_hc1']

df['black_equity'] = df['hc1_eq_male_black'] + df['hc1_eq_fem_black'] + df['hc1_eq_nb_black'] + df['hc1_eq_nogen_black']

df['black_equity_proportion'] = df['black_equity'] / df['total_hc1']

df['black_nonequity'] = df['hc1_noneq_male_black'] + df['hc1_noneq_fem_black'] + df['hc1_noneq_nb_black'] + df['hc1_noneq_nogen_black']

df['black_nonequity_proportion'] = df['black_nonequity'] / df['total_hc1']

df['black_other'] = df['hc1_other_male_black'] + df['hc1_other_fem_black'] + df['hc1_other_nb_black'] + df['hc1_other_nogen_black']

df['black_other_proportion'] = df['black_other'] / df['total_hc1']

df['black_associate'] = df['hc1_assoc_male_black'] + df['hc1_assoc_fem_black'] + df['hc1_assoc_nb_black'] + df['hc1_assoc_nogen_black']

df['black_associate_proportion'] = df['black_associate'] / df['total_hc1']

df['black_female'] = df['hc1_part_fem_black'] + df['hc1_eq_fem_black'] + df['hc1_noneq_fem_black'] + df['hc1_assoc_fem_black'] + df['hc1_other_fem_black']

df['black_female_proportion'] = df['black_female'] / df['total_hc1']

df['black_female_partner'] = df['hc1_part_fem_black']

df['black_female_partner_proportion'] = df['black_female_partner'] / df['total_hc1']

df['black_female_equity'] = df['hc1_eq_fem_black']

df['black_female_equity_proportion'] = df['black_female_equity'] / df['total_hc1']

df['black_female_nonequity'] = df['hc1_noneq_fem_black']

df['black_female_nonequity_proportion'] = df['black_female_nonequity'] / df['total_hc1']

df['black_female_other'] = df['hc1_other_fem_black']

df['black_female_other_proportion'] = df['black_female_other'] / df['total_hc1']

df['black_female_associate'] = df['hc1_assoc_fem_black']

df['black_female_associate_proportion'] = df['black_female_associate'] / df['total_hc1']

df['asian'] = df['hc1_part_male_asian'] + df['hc1_part_fem_asian'] + df['hc1_eq_male_asian'] + df['hc1_eq_fem_asian'] + df['hc1_eq_nb_asian'] + df['hc1_eq_nogen_asian'] + df['hc1_noneq_male_asian'] + df['hc1_noneq_fem_asian'] + df['hc1_noneq_nb_asian'] + df['hc1_noneq_nogen_asian'] + df['hc1_assoc_male_asian'] + df['hc1_assoc_fem_asian'] + df['hc1_assoc_nb_asian'] + df['hc1_assoc_nogen_asian'] + df['hc1_other_male_asian'] + df['hc1_other_fem_asian'] + df['hc1_other_nb_asian'] +df['hc1_other_nogen_asian']

df['asian_proportion'] = df['asian'] / df['total_hc1']

df['asian_partner'] = df['hc1_part_male_asian'] + df['hc1_part_fem_asian']

df['asian_partner_proportion'] = df['asian_partner'] / df['total_hc1']

df['asian_equity'] = df['hc1_eq_male_asian'] + df['hc1_eq_fem_asian'] + df['hc1_eq_nb_asian'] + df['hc1_eq_nogen_asian']

df['asian_equity_proportion'] = df['asian_equity'] / df['total_hc1']

df['asian_nonequity'] = df['hc1_noneq_male_asian'] + df['hc1_noneq_fem_asian'] + df['hc1_noneq_nb_asian'] + df['hc1_noneq_nogen_asian']

df['asian_nonequity_proportion'] = df['asian_nonequity'] / df['total_hc1']

df['asian_other'] = df['hc1_other_male_asian'] + df['hc1_other_fem_asian'] + df['hc1_other_nb_asian'] + df['hc1_other_nogen_asian']

df['asian_other_proportion'] = df['asian_other'] / df['total_hc1']

df['asian_associate'] = df['hc1_assoc_male_asian'] + df['hc1_assoc_fem_asian'] + df['hc1_assoc_nb_asian'] + df['hc1_assoc_nogen_asian']

df['asian_associate_proportion'] = df['asian_associate'] / df['total_hc1']

df['asian_female'] = df['hc1_part_fem_asian'] + df['hc1_eq_fem_asian'] + df['hc1_assoc_fem_asian'] + df['hc1_other_fem_asian']

df['asian_female_proportion'] = df['asian_female'] / df['total_hc1']

df['asian_female_partner'] = df['hc1_part_fem_asian']

df['asian_female_partner_proportion'] = df['hc1_part_fem_asian'] / df['total_hc1']

df['asian_female_equity'] = df['hc1_eq_fem_asian']

df['asian_female_equity_proportion'] = df['hc1_eq_fem_asian'] / df['total_hc1']

df['asian_female_nonequity'] = df['hc1_noneq_fem_asian']

df['asian_female_nonequity_proportion'] = df['hc1_noneq_fem_asian'] / df['total_hc1']

df['asian_female_other'] = df['hc1_other_fem_asian']

df['asian_female_other_proportion'] = df['hc1_other_fem_asian'] / df['total_hc1']

df['asian_female_associate'] = df['hc1_assoc_fem_asian']

df['asian_female_associate_proportion'] = df['hc1_assoc_fem_asian'] / df['total_hc1']

df['pacific_islander'] = df['hc1_part_male_pi'] + df['hc1_part_fem_pi'] + df['hc1_eq_male_pi'] + df['hc1_eq_fem_pi'] + df['hc1_eq_nb_pi'] + df['hc1_eq_nogen_pi'] + df['hc1_noneq_male_pi'] + df['hc1_noneq_fem_pi'] + df['hc1_noneq_nb_pi'] + df['hc1_noneq_nogen_pi'] + df['hc1_assoc_male_pi'] + df['hc1_assoc_fem_pi'] + df['hc1_assoc_nb_pi'] + df['hc1_assoc_nogen_pi'] + df['hc1_other_male_pi'] + df['hc1_other_fem_pi'] + df['hc1_other_nb_pi'] + df['hc1_other_nogen_pi']

df['pacific_islander_proportion'] = df['pacific_islander'] / df['total_hc1']

df['pacific_islander_partner'] = df['hc1_part_male_pi'] + df['hc1_part_fem_pi']

df['pacific_islander_partner_proportion'] = df['pacific_islander_partner'] / df['total_hc1']

df['pacific_islander_equity'] = df['hc1_eq_male_pi'] + df['hc1_eq_fem_pi'] + df['hc1_eq_nb_pi'] + df['hc1_eq_nogen_pi']

df['pacific_islander_equity_proportion'] = df['pacific_islander_equity'] / df['total_hc1']

df['pacific_islander_nonequity'] = df['hc1_noneq_male_pi'] + df['hc1_noneq_fem_pi'] + df['hc1_noneq_nb_pi'] + df['hc1_noneq_nogen_pi']

df['pacific_islander_nonequity_proportion'] = df['pacific_islander_nonequity'] / df['total_hc1']

df['pacific_islander_other'] = df['hc1_other_male_pi'] + df['hc1_other_fem_pi'] + df['hc1_other_nb_pi'] + df['hc1_other_nogen_pi']

df['pacific_islander_other_proportion'] = df['pacific_islander_other'] / df['total_hc1']

df['pacific_islander_associate'] = df['hc1_assoc_male_pi'] + df['hc1_assoc_fem_pi'] + df['hc1_assoc_nb_pi'] + df['hc1_assoc_nogen_pi']

df['pacific_islander_associate_proportion'] = df['pacific_islander_associate'] / df['total_hc1']

df['pacific_islander_female'] = df['hc1_part_fem_pi'] + df['hc1_eq_fem_pi'] + df['hc1_noneq_fem_pi'] + df['hc1_assoc_fem_pi'] + df['hc1_other_fem_pi']

df['pacific_islander_female_proportion'] = df['pacific_islander_female'] / df['total_hc1']

df['pacific_islander_female_partner'] = df['hc1_part_fem_pi']

df['pacific_islander_female_partner_proportion'] = df['pacific_islander_female_partner'] / df['total_hc1']

df['pacific_islander_female_equity'] = df['hc1_eq_fem_pi']

df['pacific_islander_female_equity_proportion'] = df['pacific_islander_female_equity'] / df['total_hc1']

df['pacific_islander_female_nonequity'] = df['hc1_noneq_fem_pi']

df['pacific_islander_female_nonequity_proportion'] = df['pacific_islander_female_nonequity'] / df['total_hc1']

df['pacific_islander_female_other'] = df['hc1_other_fem_pi']

df['pacific_islander_female_other_proportion'] = df['pacific_islander_female_other'] / df['total_hc1']

df['pacific_islander_female_associate'] = df['hc1_assoc_fem_pi']

df['pacific_islander_female_associate_proportion'] = df['hc1_assoc_fem_pi'] / df['total_hc1']

df.to_csv('total_hc_diversity.csv')
df = pd.read_csv('total_hc_diversity.csv')

df['native'] = df['hc1_part_male_nata'] + df['hc1_part_fem_nata'] + df['hc1_eq_male_nata'] + df['hc1_eq_fem_nata'] + df['hc1_eq_nb_nata'] + df['hc1_eq_nogen_nata'] + df['hc1_noneq_male_nata'] + df['hc1_noneq_fem_nata'] + df['hc1_noneq_nb_nata'] + df['hc1_noneq_nogen_nata'] + df['hc1_assoc_male_nata'] + df['hc1_assoc_fem_nata'] + df['hc1_assoc_nb_nata'] + df['hc1_assoc_nogen_nata'] + df['hc1_other_male_nata'] + df['hc1_other_fem_nata'] + df['hc1_other_nb_nata'] + df['hc1_other_nogen_nata']

df['native_proportion'] = df['native'] / df['total_hc1']

df['native_partner'] = df['hc1_part_male_nata'] + df['hc1_part_fem_nata']

df['native_partner_proportion'] = df['native_partner'] / df['total_hc1']

df['native_equity'] = df['hc1_eq_male_nata'] + df['hc1_eq_fem_nata'] + df['hc1_eq_nb_nata'] + df['hc1_eq_nogen_nata']

df['native_equity_proportion'] = df['native_equity'] / df['total_hc1']

df['native_nonequity'] = df['hc1_noneq_male_nata'] + df['hc1_noneq_fem_nata'] + df['hc1_noneq_nb_nata'] + df['hc1_noneq_nogen_nata']

df['native_nonequity_proportion'] = df['native_nonequity'] / df['total_hc1']

df['native_other'] = df['hc1_other_male_nata'] + df['hc1_other_fem_nata'] + df['hc1_other_nb_nata'] + df['hc1_other_nogen_nata']

df['native_other_proportion'] = df['native_other'] / df['total_hc1']

df['native_associate'] = df['hc1_assoc_male_nata'] + df['hc1_assoc_fem_nata'] + df['hc1_assoc_nb_nata'] + df['hc1_assoc_nogen_nata']

df['native_associate_proportion'] = df['native_associate'] / df['total_hc1']

df['native_female'] = df['hc1_part_fem_nata'] + df['hc1_eq_fem_nata'] + df['hc1_noneq_fem_nata'] + df['hc1_assoc_fem_nata'] + df['hc1_other_fem_nata']

df['native_female_proportion'] = df['native_female'] / df['total_hc1']

df['native_female_partner'] = df['hc1_part_fem_nata']

df['native_female_partner_proportion'] = df['native_female_partner'] / df['total_hc1']

df['native_female_equity'] = df['hc1_eq_fem_nata']

df['native_female_equity_proportion'] = df['native_female_equity'] / df['total_hc1']

df['native_female_other'] = df['hc1_other_fem_nata']

df['native_female_other_proportion'] = df['native_female_other'] / df['total_hc1']

df['native_female_associate'] = df['hc1_assoc_fem_nata']

df['native_female_associate_proportion'] = df['native_female_associate'] / df['total_hc1']

df['two_race'] = df['hc1_part_male_tomr'] + df['hc1_part_fem_tomr'] + df['hc1_eq_male_tomr'] + df['hc1_eq_fem_tomr'] + df['hc1_eq_nogen_tomr'] + df['hc1_noneq_male_tomr'] + df['hc1_noneq_fem_tomr'] + df['hc1_noneq_nb_tomr'] + df['hc1_noneq_nogen_tomr'] + df['hc1_assoc_male_tomr'] + df['hc1_assoc_fem_tomr'] + df['hc1_assoc_nb_tomr'] + df['hc1_assoc_nogen_tomr'] + df['hc1_other_male_tomr'] + df['hc1_other_fem_tomr'] + df['hc1_other_nb_tomr'] + df['hc1_other_nogen_tomr']

df['two_race_proportion'] = df['two_race'] / df['total_hc1']

df['two_race_partner'] = df['hc1_part_male_tomr'] + df['hc1_part_fem_tomr']

df['two_race_partner_proportion'] = df['two_race_partner'] / df['total_hc1']

df['two_race_equity'] = df['hc1_eq_male_tomr'] + df['hc1_eq_fem_tomr'] + df['hc1_eq_nb_tomr'] + df['hc1_eq_nogen_tomr']

df['two_race_equity_proportion'] = df['two_race_equity'] / df['total_hc1']

df['two_race_nonequity'] = df['hc1_noneq_male_tomr'] + df['hc1_noneq_fem_tomr'] + df['hc1_noneq_nb_tomr'] + df['hc1_noneq_nogen_tomr']

df['two_race_nonequity_proportion'] = df['two_race_nonequity'] / df['total_hc1']

df['two_race_other'] = df['hc1_other_male_tomr'] + df['hc1_other_fem_tomr'] + df['hc1_other_nb_tomr'] + df['hc1_other_nogen_tomr']

df['two_race_other_proportion'] = df['two_race_other'] / df['total_hc1']

df['two_race_associate'] = df['hc1_assoc_male_tomr'] + df['hc1_assoc_fem_tomr'] + df['hc1_assoc_nb_tomr'] + df['hc1_assoc_nogen_tomr']

df['two_race_associate_proportion'] = df['two_race_associate'] / df['total_hc1']

df['two_race_female'] = df['hc1_part_fem_tomr'] + df['hc1_eq_fem_tomr'] + df['hc1_noneq_fem_tomr'] + df['hc1_assoc_fem_tomr'] + df['hc1_other_fem_tomr']

df['two_race_female_proportion'] = df['two_race_female'] / df['total_hc1']

df['two_race_female_partner'] = df['hc1_part_fem_tomr']

df['two_race_female_partner_proportion'] = df['two_race_female_partner'] / df['total_hc1']

df['two_race_female_equity'] = df['hc1_eq_fem_tomr']

df['two_race_female_equity_proportion'] = df['two_race_female_equity'] / df['total_hc1']

df['two_race_female_nonequity'] = df['hc1_noneq_fem_tomr']

df['two_race_female_nonequity_proportion'] = df['two_race_female_nonequity'] / df['total_hc1']

df['two_race_female_other'] = df['hc1_other_fem_tomr']

df['two_race_female_other_proportion'] = df['two_race_female_other'] / df['total_hc1']

df['two_race_female_associate'] = df['hc1_assoc_fem_tomr']

df['two_race_female_associate_proportion'] = df['two_race_female_associate'] / df['total_hc1']

df.to_csv('total_hc_diversity.csv')
