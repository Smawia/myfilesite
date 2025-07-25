from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('articles',views.studies,name='studies'),
    path('contact',views.contact,name='contact'),
    path('publications/journals',views.patrols,name='patrols'),
    path('showDetailStudies',views.showDetailStudies,name='showDetailStudies'),
    path('showDetailPatrols',views.showDetailPatrols,name='showDetailPatrols'),
    path('showDetailNews',views.showDetailNews,name='showDetailNews'),
    path('pushStudyPost',views.pushStudyPost,name='pushStudyPost'),
    path('pushPatrolPost',views.pushPatrolPost,name='pushPatrolPost'),
    path('pushNewsPost',views.pushNewsPost,name='pushNewsPost'),
    path('articles/firstStudyPage',views.firstpage,name='firstpage'),
    path('articles/administrativeReform',views.administrative_reform,name='administrativereform'),
    path('articles/reformMethodology',views.reform_methodology,name='reformmethodology'),
    path('articles/NotesReform',views.Notes_reform,name='Notesreform'),
    path('articles/StudyOfUS',views.study_of_US,name='studyOfUS'),
    path('articles/StudySingapore',views.studysingapore,name='studysingapore'),
    path('articles/StudyRwanda',views.rwanda_study,name='rwanda_study'),
    path('articles/StudyChina',views.china_study,name='china_study'),
    path('articles/MalaysiaStudy',views.malaysia_study,name='malaysia_study'),
    path('articles/JordanStudy',views.jor_study,name='jor_study'),
    path('articles/FeaturesOfAdministrativeReformInYemen',views.features_of_administrative_reform_in_yemen,name='features_of_administrative_reform_in_yemen'),
    path('articles/ComprehensiveReform',views.comprehensive_reform,name='comprehensive_reform'),
    path('articles/AdministrativeRaw',views.administrative_raw,name='administrative_raw'),
    path('articles/AdministrativeReformTwo',views.administrative_reform2,name='administrative_reform2'),
    path('articles/AdministrativeLawInYemen',views.administrative_law_in_yemen,name='administrative_law_in_yemen'),
    path('articles/GlobalManagementReform',views.global_management_reform,name='global_management_reform'),
    path('articles/FutureForReformingAdministrativeLawInYemen',views.future_fo_reforming_administrative_law_in_yemen,name='future_fo_reforming_administrative_law_in_yemen'),
    path('articles/LegalReform',views.legal_reform,name='legal_reform'),
    path('articles/EvolutionOfPublicAdministration',views.evolution_of_public_administration,name='evolution_of_public_administration'),
    path('articles/StagesOfLegislativeReform',views.stages_of_legislative_reform,name='stages_of_legislative_reform'),
    path('articles/LegislativeReformInTheWorld',views.legislative_reform_in_the_world,name='legislative_reform_in_the_world'),
    path('articles/LegalReformInYemen',views.legal_reform_in_yemen,name='legal_reform_in_yemen'),
    path('articles/GeneralAdministrationInYemen',views.general_administration_in_yemen,name='general_administration_in_yemen'),
    path('publications/books',views.books,name='books'),
    path('journals/osus/articles/', views.journal_studies, name='journal_studies'),
    path('journals/osus/articles/SocialMarketEconomy', views.social_market_economy, name='social_market_economy'),
    path('journals/osus/articles/AgriculturalRenaissanceInYemen', views.agricultural_renaissance_in_yemen, name='agricultural_renaissance_in_yemen'),
    path('journals/osus/articles/JudiciaryInYemen', views.judiciary_in_yemen, name='judiciary_in_yemen'),
    path('journals/osus/articles/JobsInYemen', views.jobs_in_yemen, name='jobs_in_yemen'),
    path('journals/osus/articles/HygieneAndSolidWasteManagement', views.hygiene_and_solid_waste_management, name='hygiene_and_solid_waste_management'),
    path('journals/osus/articles/EducationalSystemInYemen', views.educational_system_in_yemen, name='educational_system_in_yemen'),
    path('journals/osus/articles/BeggingPhenomenonInYemen', views.begging_phenomenon_in_yemen, name='begging_phenomenon_in_yemen'),
    path('journals/osus/articles/LocalGovernanceInYemen', views.local_governance_in_yemen, name='local_governance_in_yemen'),

    # new studies
    path('articles/CurrentEconomicSituation',views.current_economic_situation,name='current_economic_situation'),
    path('articles/theExistingSocialSituation',views.the_existing_social_situation,name='the_existing_social_situation'),
    path('articles/TheBureaucraticApparatusOnAdministrativeReform',views.the_influence_of_the_bureaucratic_apparatus_on_administrative_reform,name='the_influence_of_the_bureaucratic_apparatus_on_administrative_reform'),
    path('articles/PublicFinanceAndEconomicConstruction',views.public_finance_and_economic_construction,name='public_finance_and_economic_construction'),
    path('articles/FinancialReformInCountries',views.financial_reform_in_countries,name='financial_reform_in_countries'),
    path('articles/FinancialReformInYemen',views.financial_reform_in_yemen,name='financial_reform_in_yemen'),
    path('articles/FutureOfFinancialReformInYemen',views.future_of_financial_reform_in_yemen,name='future_of_financial_reform_in_yemen'),
    path('articles/PrivateSectorInYemen',views.the_private_sector_inyemen,name='the_private_sector_inyemen'),
    path('articles/RoleOfThePrivateSectorInWorld',views.role_of_the_private_sector_in_world,name='role_of_the_private_sector_in_world'),
    path('articles/RoleOfPrivateSectorInDevelopment',views.role_of_the_private_sector_in_development_in_yemen,name='role_of_the_private_sector_in_development_in_yemen'),
    path('articles/FutureOfPrivateSectorInYemen',views.future_of_private_sector_in_Yemen,name='future_of_private_sector_in_Yemen'),
    path('articles/Government',views.Government,name='E-Government'),
    path('articles/implementingE-government',views.implementing_egovernment,name='implementing_e-government'),
    path('articles/GlobalExperiencesInEgovernment',views.global_experiences_in_egovernment,name='global_experiences_in_egovernment'),
    path('articles/InformationCommunicationsTechnologyInYemen',views.information_and_communications_technology_in_Yemen,name='information_and_communications_technology_in_Yemen'),
    path('articles/ImplementingEgovernmentInYemen',views.implementing_egovernment_in_Yemen,name='implementing_e-government_in_Yemen'),
    path('articles/FutureEGovernmentYemen',views.future_of_eGovernment_Yemen,name='future_of_eGovernment_Yemen'),
    path('download/', views.download_or_view_file, name='download_or_view_file'),
    path('publications/journals/osus/osus-2025-03-issue.pdf', views.download_or_view_patrols, name='download_or_view_patrols'),
    path('publications/journals/osus/Second-Osus-2025-06-Issue.pdf', views.download_or_view_second_ossus, name='download_or_view_second_ossus'),
    path('publications', views.show_publications, name='publications'),
    path('publications/Journals/Osus', views.osus_journals, name='osus'),
    path('publications/Journals/Osus/osus-2025-03-issue-contents.pdf', views.view_osus_content, name='osus-content'),
    path('publications/Journals/Osus/osus-2025-06-issue-contents.pdf', views.view_osus_second_content, name='osus-second-content'),
    path('Infographics/', views.view_infograph, name='infographs'),
    path('infographics/<slug:slug>/', views.infograph_detail, name='infograph_detail'),
]
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]