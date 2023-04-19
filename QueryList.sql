select VF_CONFIG_CUR_RATES_FUNC ('8','102.77','840','USD to Albanian Lek','19/04/2023') from dual;
select VF_CONFIG_CUR_RATES_FUNC ('8','112.3','978','EUR to Albanian Lek','19/04/2023') from dual;
select * from vf_config_cur_rates_t where effective_date in ('19/04/2023');

