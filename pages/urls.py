from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap


urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('studies',views.studies,name='studies'),
    path('contact',views.contact,name='contact'),
    path('patrols',views.patrols,name='patrols'),
    path('showDetailStudies',views.showDetailStudies,name='showDetailStudies'),
    path('showDetailPatrols',views.showDetailPatrols,name='showDetailPatrols'),
    path('showDetailNews',views.showDetailNews,name='showDetailNews'),
    path('pushStudyPost',views.pushStudyPost,name='pushStudyPost'),
    path('pushPatrolPost',views.pushPatrolPost,name='pushPatrolPost'),
    path('pushNewsPost',views.pushNewsPost,name='pushNewsPost'),
    path('firstStudyPage',views.firstpage,name='firstpage'),
    path('administrativeReform',views.administrative_reform,name='administrativereform'),
    path('reformMethodology',views.reform_methodology,name='reformmethodology'),
    path('NotesReform',views.Notes_reform,name='Notesreform'),
    path('StudyOfUS',views.study_of_US,name='studyOfUS'),
    path('StudySingapore',views.studysingapore,name='studysingapore'),
    path('StudyRwanda',views.rwanda_study,name='rwanda_study'),
    path('StudyChina',views.china_study,name='china_study'),
    path('MalaysiaStudy',views.malaysia_study,name='malaysia_study'),
    path('JordanStudy',views.jor_study,name='jor_study'),
    path('FeaturesOfAdministrativeReformInYemen',views.features_of_administrative_reform_in_yemen,name='features_of_administrative_reform_in_yemen'),
    path('ComprehensiveReform',views.comprehensive_reform,name='comprehensive_reform'),
    path('AdministrativeRaw',views.administrative_raw,name='administrative_raw'),
    path('AdministrativeReformTwo',views.administrative_reform2,name='administrative_reform2'),
    path('AdministrativeLawInYemen',views.administrative_law_in_yemen,name='administrative_law_in_yemen'),
    path('GlobalManagementReform',views.global_management_reform,name='global_management_reform'),
    path('FutureForReformingAdministrativeLawInYemen',views.future_fo_reforming_administrative_law_in_yemen,name='future_fo_reforming_administrative_law_in_yemen'),
    path('LegalReform',views.legal_reform,name='legal_reform'),
    path('EvolutionOfPublicAdministration',views.evolution_of_public_administration,name='evolution_of_public_administration'),
    path('StagesOfLegislativeReform',views.stages_of_legislative_reform,name='stages_of_legislative_reform'),
    path('LegislativeReformInTheWorld',views.legislative_reform_in_the_world,name='legislative_reform_in_the_world'),
    path('LegalReformInYemen',views.legal_reform_in_yemen,name='legal_reform_in_yemen'),
    path('GeneralAdministrationInYemen',views.general_administration_in_yemen,name='general_administration_in_yemen'),
    path('Books',views.books,name='books'),

    # new studies
    path('CurrentEconomicSituation',views.current_economic_situation,name='current_economic_situation'),
    path('theExistingSocialSituation',views.the_existing_social_situation,name='the_existing_social_situation'),
    path('TheBureaucraticApparatusOnAdministrativeReform',views.the_influence_of_the_bureaucratic_apparatus_on_administrative_reform,name='the_influence_of_the_bureaucratic_apparatus_on_administrative_reform'),
    path('PublicFinanceAndEconomicConstruction',views.public_finance_and_economic_construction,name='public_finance_and_economic_construction'),
    path('FinancialReformInCountries',views.financial_reform_in_countries,name='financial_reform_in_countries'),
    path('FinancialReformInYemen',views.financial_reform_in_yemen,name='financial_reform_in_yemen'),
    path('FutureOfFinancialReformInYemen',views.future_of_financial_reform_in_yemen,name='future_of_financial_reform_in_yemen'),
    path('PrivateSectorInYemen',views.the_private_sector_inyemen,name='the_private_sector_inyemen'),
    path('RoleOfThePrivateSectorInWorld',views.role_of_the_private_sector_in_world,name='role_of_the_private_sector_in_world'),
    path('RoleOfPrivateSectorInDevelopment',views.role_of_the_private_sector_in_development_in_yemen,name='role_of_the_private_sector_in_development_in_yemen'),
    path('FutureOfPrivateSectorInYemen',views.future_of_private_sector_in_Yemen,name='future_of_private_sector_in_Yemen'),
    path('Government',views.Government,name='E-Government'),
    path('implementingE-government',views.implementing_egovernment,name='implementing_e-government'),
    path('GlobalExperiencesInEgovernment',views.global_experiences_in_egovernment,name='global_experiences_in_egovernment'),
    path('InformationCommunicationsTechnologyInYemen',views.information_and_communications_technology_in_Yemen,name='information_and_communications_technology_in_Yemen'),
    path('ImplementingEgovernmentInYemen',views.implementing_egovernment_in_Yemen,name='implementing_e-government_in_Yemen'),
    path('FutureEGovernmentYemen',views.future_of_eGovernment_Yemen,name='future_of_eGovernment_Yemen'),
    path('download/', views.download_or_view_file, name='download_or_view_file'),
]
sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns += [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]