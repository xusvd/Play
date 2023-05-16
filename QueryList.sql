select VF_CONFIG_CUR_RATES_FUNC ('8','102.71','840','USD to Albanian Lek','16/05/2023') from dual;
select VF_CONFIG_CUR_RATES_FUNC ('8','111.89','978','EUR to Albanian Lek','16/05/2023') from dual;
select * from vf_config_cur_rates_t where effective_date in ('16/05/2023');

