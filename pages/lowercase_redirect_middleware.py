from django.shortcuts import redirect

class InfographicsRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # تعريف جميع الروابط الثابتة الرسمية مع الحالة الصحيحة
        self.correct_paths = {
            '/': '/',
            '/about': '/about',
            '/articles': '/articles',
            '/contact': '/contact',
            '/publications/journals': '/publications/journals',
            '/showDetailStudies': '/showDetailStudies',
            '/showDetailPatrols': '/showDetailPatrols',
            '/showDetailNews': '/showDetailNews',
            '/pushStudyPost': '/pushStudyPost',
            '/pushPatrolPost': '/pushPatrolPost',
            '/pushNewsPost': '/pushNewsPost',
            '/articles/firstStudyPage': '/articles/firstStudyPage',
            '/articles/administrativeReform': '/articles/administrativeReform',
            '/articles/reformMethodology': '/articles/reformMethodology',
            '/articles/NotesReform': '/articles/NotesReform',
            '/articles/StudyOfUS': '/articles/StudyOfUS',
            '/articles/StudySingapore': '/articles/StudySingapore',
            '/articles/StudyRwanda': '/articles/StudyRwanda',
            '/articles/StudyChina': '/articles/StudyChina',
            '/articles/MalaysiaStudy': '/articles/MalaysiaStudy',
            '/articles/JordanStudy': '/articles/JordanStudy',
            '/articles/FeaturesOfAdministrativeReformInYemen': '/articles/FeaturesOfAdministrativeReformInYemen',
            '/articles/ComprehensiveReform': '/articles/ComprehensiveReform',
            '/articles/AdministrativeRaw': '/articles/AdministrativeRaw',
            '/articles/AdministrativeReformTwo': '/articles/AdministrativeReformTwo',
            '/articles/AdministrativeLawInYemen': '/articles/AdministrativeLawInYemen',
            '/articles/GlobalManagementReform': '/articles/GlobalManagementReform',
            '/articles/FutureForReformingAdministrativeLawInYemen': '/articles/FutureForReformingAdministrativeLawInYemen',
            '/articles/LegalReform': '/articles/LegalReform',
            '/articles/EvolutionOfPublicAdministration': '/articles/EvolutionOfPublicAdministration',
            '/articles/StagesOfLegislativeReform': '/articles/StagesOfLegislativeReform',
            '/articles/LegislativeReformInTheWorld': '/articles/LegislativeReformInTheWorld',
            '/articles/LegalReformInYemen': '/articles/LegalReformInYemen',
            '/articles/GeneralAdministrationInYemen': '/articles/GeneralAdministrationInYemen',
            '/publications/books': '/publications/books',
            '/journals/osus/articles/': '/journals/osus/articles/',
            '/journals/osus/articles/SocialMarketEconomy': '/journals/osus/articles/SocialMarketEconomy',
            '/journals/osus/articles/AgriculturalRenaissanceInYemen': '/journals/osus/articles/AgriculturalRenaissanceInYemen',
            '/journals/osus/articles/JudiciaryInYemen': '/journals/osus/articles/JudiciaryInYemen',
            '/journals/osus/articles/JobsInYemen': '/journals/osus/articles/JobsInYemen',
            '/journals/osus/articles/HygieneAndSolidWasteManagement': '/journals/osus/articles/HygieneAndSolidWasteManagement',
            '/journals/osus/articles/EducationalSystemInYemen': '/journals/osus/articles/EducationalSystemInYemen',
            '/journals/osus/articles/BeggingPhenomenonInYemen': '/journals/osus/articles/BeggingPhenomenonInYemen',
            '/journals/osus/articles/LocalGovernanceInYemen': '/journals/osus/articles/LocalGovernanceInYemen',
            '/journals/osus/articles/EffectivenessOfTheJudicialAndOversightSystemInYemen': '/journals/osus/articles/EffectivenessOfTheJudicialAndOversightSystemInYemen',
            '/journals/osus/articles/SocialHealthInsuranceInYemen': '/journals/osus/articles/SocialHealthInsuranceInYemen',
            '/articles/CurrentEconomicSituation': '/articles/CurrentEconomicSituation',
            '/articles/theExistingSocialSituation': '/articles/theExistingSocialSituation',
            '/articles/TheBureaucraticApparatusOnAdministrativeReform': '/articles/TheBureaucraticApparatusOnAdministrativeReform',
            '/articles/PublicFinanceAndEconomicConstruction': '/articles/PublicFinanceAndEconomicConstruction',
            '/articles/FinancialReformInCountries': '/articles/FinancialReformInCountries',
            '/articles/FinancialReformInYemen': '/articles/FinancialReformInYemen',
            '/articles/FutureOfFinancialReformInYemen': '/articles/FutureOfFinancialReformInYemen',
            '/articles/PrivateSectorInYemen': '/articles/PrivateSectorInYemen',
            '/articles/RoleOfThePrivateSectorInWorld': '/articles/RoleOfThePrivateSectorInWorld',
            '/articles/RoleOfPrivateSectorInDevelopment': '/articles/RoleOfPrivateSectorInDevelopment',
            '/articles/FutureOfPrivateSectorInYemen': '/articles/FutureOfPrivateSectorInYemen',
            '/articles/Government': '/articles/Government',
            '/articles/implementingE-government': '/articles/implementingE-government',
            '/articles/GlobalExperiencesInEgovernment': '/articles/GlobalExperiencesInEgovernment',
            '/articles/InformationCommunicationsTechnologyInYemen': '/articles/InformationCommunicationsTechnologyInYemen',
            '/articles/ImplementingEgovernmentInYemen': '/articles/ImplementingEgovernmentInYemen',
            '/articles/FutureEGovernmentYemen': '/articles/FutureEGovernmentYemen',
            '/download/': '/download/',
            '/publications/journals/osus/osus-2025-03-issue.pdf': '/publications/journals/osus/osus-2025-03-issue.pdf',
            '/publications/journals/osus/Second-Osus-2025-06-Issue.pdf': '/publications/journals/osus/Second-Osus-2025-06-Issue.pdf',
            '/publications': '/publications',
            '/publications/Journals/Osus': '/publications/Journals/Osus',
            '/publications/Journals/Osus/osus-2025-03-issue-contents.pdf': '/publications/Journals/Osus/osus-2025-03-issue-contents.pdf',
            '/publications/Journals/Osus/osus-2025-06-issue-contents.pdf': '/publications/Journals/Osus/osus-2025-06-issue-contents.pdf',
            '/Infographics/': '/Infographics/',
        }

    def __call__(self, request):
        path = request.path
        

        # تحقق إذا بدأ المسار بـ /infographics/ بأحرف صغيرة (غير رسمي)
        if path.lower().startswith('/infographics/') and not path.startswith('/Infographics/'):
            # استبدال بداية المسار إلى الشكل الرسمي
            new_path = '/Infographics/' + path[len('/infographics/'):]
            # أضف استعلامات GET لو وجدت
            if request.META.get('QUERY_STRING'):
                new_path += '?' + request.META['QUERY_STRING']
            return redirect(new_path, permanent=True)

        # تحقق إذا الرابط نفسه /infographics بدون / في النهاية
        if path.lower() == '/infographics' and path != '/Infographics':
            return redirect('/Infographics', permanent=True)
        
        # معالجة باقي الروابط الثابتة
        for correct_path_lower, correct_path_real in self.correct_paths.items():
            if path.lower() == correct_path_lower.lower():
                if path != correct_path_real:
                    final_path = correct_path_real
                    if request.META.get('QUERY_STRING'):
                        final_path += '?' + request.META['QUERY_STRING']
                    return redirect(final_path, permanent=True)
                break

        return self.get_response(request)
