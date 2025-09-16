import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint

class TemabaruPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, "templates")
        toolkit.add_public_directory(config_, "public")
        toolkit.add_resource("assets", "temabaru")

    # Tambah route baru disini lewat Blueprint
    def get_blueprint(self):
        blueprint = Blueprint('temabaru', __name__)
        
        # Route Regulasi
        @blueprint.route('/regulasi')
        def regulasi():
            return toolkit.render('regulasi/index.html')

        # Halaman Asta Cita Presiden
        @blueprint.route('/asta-cita-presiden')
        def asta_cita_presiden():
            return toolkit.render('asta-cita-presiden/index.html')
        
        #Halaman Berita
        @blueprint.route('/berita')
        def berita():
            return toolkit.render('berita/index.html')
        
        #Halaman Program Unggulan Bupati
        @blueprint.route('/program-unggulan-bupati')
        def program_unggulan_bupati():
            return toolkit.render('program-unggulan-bupati/index.html')

        return blueprint


class CustomGroupPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.ITemplateHelpers)

    def get_helpers(self):
        return {
            'latest_group_datasets': self.latest_group_datasets
        }

    def latest_group_datasets(self, group_name, limit=3):
        context = {
            'model': toolkit.model,
            'session': toolkit.model.Session,
            'user': toolkit.g.user
        }
        data_dict = {
            'q': f'groups:{group_name}',
            'sort': 'metadata_created desc',
            'rows': limit
        }
        return toolkit.get_action('package_search')(context, data_dict)['results']
