"""This file was generated by xsdata, v24.2.1, on 2024-02-24 11:16:39

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.mdfe.bindings.v3_0.mdfe_tipos_basico_v3_00 import TretMdfe

__NAMESPACE__ = "http://www.portalfiscal.inf.br/mdfe"


@dataclass
class RetMdfe(TretMdfe):
    """
    Manisfesto Eletrônico de Documentos Fiscais.
    """

    class Meta:
        name = "retMDFe"
        namespace = "http://www.portalfiscal.inf.br/mdfe"
