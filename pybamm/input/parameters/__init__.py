import lazy_loader


__getattr__, __dir__, __all__ = lazy_loader.attach(
    __name__,
    submodules={
        'ecm',
        'lead_acid',
        'lithium_ion',
    },
    submod_attrs={
        'ecm': [
            'c1',
            'c1_data',
            'dUdT',
            'dUdT_data',
            'example_set',
            'get_parameter_values',
            'ocv',
            'ocv_data',
            'r0',
            'r0_data',
            'r1',
            'r1_data',
        ],
        'lead_acid': [
            'Sulzer2019',
            'conductivity_Gu1997',
            'darken_thermodynamic_factor_Chapman1968',
            'diffusivity_Gu1997',
            'get_parameter_values',
            'lead_dioxide_exchange_current_density_Sulzer2019',
            'lead_dioxide_ocp_Bode1977',
            'lead_exchange_current_density_Sulzer2019',
            'lead_ocp_Bode1977',
            'oxygen_exchange_current_density_Sulzer2019',
        ],
        'lithium_ion': [
            'Ai2020',
            'Chen2020',
            'Chen2020_composite',
            'Ecker2015',
            'Ecker2015_graphite_halfcell',
            'LFP_electrolyte_exchange_current_density_kashkooli2017',
            'LFP_ocp_Afshar2017',
            'MSMR_example_set',
            'Marquis2019',
            'Mohtat2020',
            'NCA_Kim2011',
            'NMC_diffusivity_PeymanMPM',
            'NMC_electrolyte_exchange_current_density_PeymanMPM',
            'NMC_entropic_change_PeymanMPM',
            'NMC_ocp_PeymanMPM',
            'OKane2022',
            'OKane2022_graphite_SiOx_halfcell',
            'ORegan2022',
            'Prada2013',
            'Ramadass2004',
            'SEI_limited_dead_lithium_OKane2022',
            'Xu2019',
            'aluminium_heat_capacity_CRC',
            'copper_heat_capacity_CRC',
            'copper_thermal_conductivity_CRC',
            'cracking_rate_Ai2020',
            'dlnf_dlnc_Ai2020',
            'electrolyte_TDF_EC_EMC_3_7_Landesfeind2019',
            'electrolyte_TDF_base_Landesfeind2019',
            'electrolyte_conductivity_Ai2020',
            'electrolyte_conductivity_Capiglia1999',
            'electrolyte_conductivity_EC_EMC_3_7_Landesfeind2019',
            'electrolyte_conductivity_Ecker2015',
            'electrolyte_conductivity_Kim2011',
            'electrolyte_conductivity_Nyman2008',
            'electrolyte_conductivity_Nyman2008_arrhenius',
            'electrolyte_conductivity_PeymanMPM',
            'electrolyte_conductivity_Prada2013',
            'electrolyte_conductivity_Ramadass2004',
            'electrolyte_conductivity_Valoen2005',
            'electrolyte_conductivity_base_Landesfeind2019',
            'electrolyte_diffusivity_Ai2020',
            'electrolyte_diffusivity_Capiglia1999',
            'electrolyte_diffusivity_EC_EMC_3_7_Landesfeind2019',
            'electrolyte_diffusivity_Ecker2015',
            'electrolyte_diffusivity_Kim2011',
            'electrolyte_diffusivity_Nyman2008',
            'electrolyte_diffusivity_Nyman2008_arrhenius',
            'electrolyte_diffusivity_PeymanMPM',
            'electrolyte_diffusivity_Ramadass2004',
            'electrolyte_diffusivity_Valoen2005',
            'electrolyte_diffusivity_base_Landesfeind2019',
            'electrolyte_transference_number_EC_EMC_3_7_Landesfeind2019',
            'electrolyte_transference_number_base_Landesfeind2019',
            'get_parameter_values',
            'graphite_LGM50_diffusivity_Chen2020',
            'graphite_LGM50_diffusivity_ORegan2022',
            'graphite_LGM50_electrolyte_exchange_current_density_Chen2020',
            'graphite_LGM50_electrolyte_exchange_current_density_ORegan2022',
            'graphite_LGM50_entropic_change_ORegan2022',
            'graphite_LGM50_heat_capacity_ORegan2022',
            'graphite_LGM50_ocp_Chen2020',
            'graphite_LGM50_ocp_Chen2020_data',
            'graphite_LGM50_thermal_conductivity_ORegan2022',
            'graphite_cracking_rate_Ai2020',
            'graphite_diffusivity_Dualfoil1998',
            'graphite_diffusivity_Ecker2015',
            'graphite_diffusivity_Kim2011',
            'graphite_diffusivity_PeymanMPM',
            'graphite_electrolyte_exchange_current_density_Dualfoil1998',
            'graphite_electrolyte_exchange_current_density_Ecker2015',
            'graphite_electrolyte_exchange_current_density_Kim2011',
            'graphite_electrolyte_exchange_current_density_PeymanMPM',
            'graphite_electrolyte_exchange_current_density_Ramadass2004',
            'graphite_entropic_change_Moura2016',
            'graphite_entropic_change_PeymanMPM',
            'graphite_entropy_Enertech_Ai2020_function',
            'graphite_mcmb2528_diffusivity_Dualfoil1998',
            'graphite_mcmb2528_ocp_Dualfoil1998',
            'graphite_ocp_Ecker2015',
            'graphite_ocp_Enertech_Ai2020',
            'graphite_ocp_Enertech_Ai2020_data',
            'graphite_ocp_Kim2011',
            'graphite_ocp_PeymanMPM',
            'graphite_ocp_Ramadass2004',
            'graphite_volume_change_Ai2020',
            'li_metal_electrolyte_exchange_current_density_Xu2019',
            'lico2_cracking_rate_Ai2020',
            'lico2_diffusivity_Dualfoil1998',
            'lico2_diffusivity_Ramadass2004',
            'lico2_electrolyte_exchange_current_density_Dualfoil1998',
            'lico2_electrolyte_exchange_current_density_Ramadass2004',
            'lico2_entropic_change_Ai2020_function',
            'lico2_entropic_change_Moura2016',
            'lico2_ocp_Ai2020',
            'lico2_ocp_Ai2020_data',
            'lico2_ocp_Dualfoil1998',
            'lico2_ocp_Ramadass2004',
            'lico2_volume_change_Ai2020',
            'nca_diffusivity_Kim2011',
            'nca_electrolyte_exchange_current_density_Kim2011',
            'nca_ocp_Kim2011',
            'nco_diffusivity_Ecker2015',
            'nco_electrolyte_exchange_current_density_Ecker2015',
            'nco_ocp_Ecker2015',
            'nmc_LGM50_diffusivity_Chen2020',
            'nmc_LGM50_diffusivity_ORegan2022',
            'nmc_LGM50_electrolyte_exchange_current_density_Chen2020',
            'nmc_LGM50_electrolyte_exchange_current_density_ORegan2022',
            'nmc_LGM50_electronic_conductivity_ORegan2022',
            'nmc_LGM50_entropic_change_ORegan2022',
            'nmc_LGM50_heat_capacity_ORegan2022',
            'nmc_LGM50_ocp_Chen2020',
            'nmc_LGM50_thermal_conductivity_ORegan2022',
            'nmc_electrolyte_exchange_current_density_Xu2019',
            'nmc_ocp_Xu2019',
            'plating_exchange_current_density_OKane2020',
            'separator_LGM50_heat_capacity_ORegan2022',
            'silicon_LGM50_electrolyte_exchange_current_density_Chen2020',
            'silicon_ocp_delithiation_Mark2016',
            'silicon_ocp_lithiation_Mark2016',
            'stripping_exchange_current_density_OKane2020',
            'volume_change_Ai2020',
        ],
    },
)

__all__ = ['Ai2020', 'Chen2020', 'Chen2020_composite', 'Ecker2015',
           'Ecker2015_graphite_halfcell',
           'LFP_electrolyte_exchange_current_density_kashkooli2017',
           'LFP_ocp_Afshar2017', 'MSMR_example_set', 'Marquis2019',
           'Mohtat2020', 'NCA_Kim2011', 'NMC_diffusivity_PeymanMPM',
           'NMC_electrolyte_exchange_current_density_PeymanMPM',
           'NMC_entropic_change_PeymanMPM', 'NMC_ocp_PeymanMPM', 'OKane2022',
           'OKane2022_graphite_SiOx_halfcell', 'ORegan2022', 'Prada2013',
           'Ramadass2004', 'SEI_limited_dead_lithium_OKane2022', 'Sulzer2019',
           'Xu2019', 'aluminium_heat_capacity_CRC', 'c1', 'c1_data',
           'conductivity_Gu1997', 'copper_heat_capacity_CRC',
           'copper_thermal_conductivity_CRC', 'cracking_rate_Ai2020', 'dUdT',
           'dUdT_data', 'darken_thermodynamic_factor_Chapman1968',
           'diffusivity_Gu1997', 'dlnf_dlnc_Ai2020', 'ecm',
           'electrolyte_TDF_EC_EMC_3_7_Landesfeind2019',
           'electrolyte_TDF_base_Landesfeind2019',
           'electrolyte_conductivity_Ai2020',
           'electrolyte_conductivity_Capiglia1999',
           'electrolyte_conductivity_EC_EMC_3_7_Landesfeind2019',
           'electrolyte_conductivity_Ecker2015',
           'electrolyte_conductivity_Kim2011',
           'electrolyte_conductivity_Nyman2008',
           'electrolyte_conductivity_Nyman2008_arrhenius',
           'electrolyte_conductivity_PeymanMPM',
           'electrolyte_conductivity_Prada2013',
           'electrolyte_conductivity_Ramadass2004',
           'electrolyte_conductivity_Valoen2005',
           'electrolyte_conductivity_base_Landesfeind2019',
           'electrolyte_diffusivity_Ai2020',
           'electrolyte_diffusivity_Capiglia1999',
           'electrolyte_diffusivity_EC_EMC_3_7_Landesfeind2019',
           'electrolyte_diffusivity_Ecker2015',
           'electrolyte_diffusivity_Kim2011',
           'electrolyte_diffusivity_Nyman2008',
           'electrolyte_diffusivity_Nyman2008_arrhenius',
           'electrolyte_diffusivity_PeymanMPM',
           'electrolyte_diffusivity_Ramadass2004',
           'electrolyte_diffusivity_Valoen2005',
           'electrolyte_diffusivity_base_Landesfeind2019',
           'electrolyte_transference_number_EC_EMC_3_7_Landesfeind2019',
           'electrolyte_transference_number_base_Landesfeind2019',
           'example_set', 'get_parameter_values',
           'graphite_LGM50_diffusivity_Chen2020',
           'graphite_LGM50_diffusivity_ORegan2022',
           'graphite_LGM50_electrolyte_exchange_current_density_Chen2020',
           'graphite_LGM50_electrolyte_exchange_current_density_ORegan2022',
           'graphite_LGM50_entropic_change_ORegan2022',
           'graphite_LGM50_heat_capacity_ORegan2022',
           'graphite_LGM50_ocp_Chen2020', 'graphite_LGM50_ocp_Chen2020_data',
           'graphite_LGM50_thermal_conductivity_ORegan2022',
           'graphite_cracking_rate_Ai2020',
           'graphite_diffusivity_Dualfoil1998',
           'graphite_diffusivity_Ecker2015', 'graphite_diffusivity_Kim2011',
           'graphite_diffusivity_PeymanMPM',
           'graphite_electrolyte_exchange_current_density_Dualfoil1998',
           'graphite_electrolyte_exchange_current_density_Ecker2015',
           'graphite_electrolyte_exchange_current_density_Kim2011',
           'graphite_electrolyte_exchange_current_density_PeymanMPM',
           'graphite_electrolyte_exchange_current_density_Ramadass2004',
           'graphite_entropic_change_Moura2016',
           'graphite_entropic_change_PeymanMPM',
           'graphite_entropy_Enertech_Ai2020_function',
           'graphite_mcmb2528_diffusivity_Dualfoil1998',
           'graphite_mcmb2528_ocp_Dualfoil1998', 'graphite_ocp_Ecker2015',
           'graphite_ocp_Enertech_Ai2020', 'graphite_ocp_Enertech_Ai2020_data',
           'graphite_ocp_Kim2011', 'graphite_ocp_PeymanMPM',
           'graphite_ocp_Ramadass2004', 'graphite_volume_change_Ai2020',
           'lead_acid', 'lead_dioxide_exchange_current_density_Sulzer2019',
           'lead_dioxide_ocp_Bode1977',
           'lead_exchange_current_density_Sulzer2019', 'lead_ocp_Bode1977',
           'li_metal_electrolyte_exchange_current_density_Xu2019',
           'lico2_cracking_rate_Ai2020', 'lico2_diffusivity_Dualfoil1998',
           'lico2_diffusivity_Ramadass2004',
           'lico2_electrolyte_exchange_current_density_Dualfoil1998',
           'lico2_electrolyte_exchange_current_density_Ramadass2004',
           'lico2_entropic_change_Ai2020_function',
           'lico2_entropic_change_Moura2016', 'lico2_ocp_Ai2020',
           'lico2_ocp_Ai2020_data', 'lico2_ocp_Dualfoil1998',
           'lico2_ocp_Ramadass2004', 'lico2_volume_change_Ai2020',
           'lithium_ion', 'nca_diffusivity_Kim2011',
           'nca_electrolyte_exchange_current_density_Kim2011',
           'nca_ocp_Kim2011', 'nco_diffusivity_Ecker2015',
           'nco_electrolyte_exchange_current_density_Ecker2015',
           'nco_ocp_Ecker2015', 'nmc_LGM50_diffusivity_Chen2020',
           'nmc_LGM50_diffusivity_ORegan2022',
           'nmc_LGM50_electrolyte_exchange_current_density_Chen2020',
           'nmc_LGM50_electrolyte_exchange_current_density_ORegan2022',
           'nmc_LGM50_electronic_conductivity_ORegan2022',
           'nmc_LGM50_entropic_change_ORegan2022',
           'nmc_LGM50_heat_capacity_ORegan2022', 'nmc_LGM50_ocp_Chen2020',
           'nmc_LGM50_thermal_conductivity_ORegan2022',
           'nmc_electrolyte_exchange_current_density_Xu2019', 'nmc_ocp_Xu2019',
           'ocv', 'ocv_data', 'oxygen_exchange_current_density_Sulzer2019',
           'plating_exchange_current_density_OKane2020', 'r0', 'r0_data', 'r1',
           'r1_data', 'separator_LGM50_heat_capacity_ORegan2022',
           'silicon_LGM50_electrolyte_exchange_current_density_Chen2020',
           'silicon_ocp_delithiation_Mark2016',
           'silicon_ocp_lithiation_Mark2016',
           'stripping_exchange_current_density_OKane2020',
           'volume_change_Ai2020']
