"""This file was generated by xsdata, v23.6, on 2024-01-31 16:38:31

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from nfelib.cte.bindings.v4_0.cons_sit_cte_tipos_basico_v4_00 import (
    TconsSitCte,
    TretConsSitCte,
    ProcEventoCteVersao,
    ProtCteVersao,
)
from nfelib.cte.bindings.v4_0.cons_sit_cte_v4_00 import ConsSitCte
from nfelib.cte.bindings.v4_0.cons_stat_serv_cte_v4_00 import ConsStatServCte
from nfelib.cte.bindings.v4_0.cons_stat_serv_tipos_basico_v4_00 import (
    TconsStatServ,
    TretConsStatServ,
)
from nfelib.cte.bindings.v4_0.cte_modal_aereo_v4_00 import (
    Aereo,
    InfTotApUniAp,
    NatCargaCInfManu,
)
from nfelib.cte.bindings.v4_0.cte_modal_aquaviario_v4_00 import (
    Aquav,
    AquavDirec,
    AquavTpNav,
)
from nfelib.cte.bindings.v4_0.cte_modal_dutoviario_v4_00 import Duto
from nfelib.cte.bindings.v4_0.cte_modal_ferroviario_v4_00 import (
    TenderFer,
    Ferrov,
    FerrovTpTraf,
    TrafMutFerrEmi,
    TrafMutRespFat,
)
from nfelib.cte.bindings.v4_0.cte_modal_rodoviario_os_v4_00 import (
    InfFretamentoTpFretamento,
    PropTpProp,
    RodoOs,
)
from nfelib.cte.bindings.v4_0.cte_modal_rodoviario_v4_00 import Rodo
from nfelib.cte.bindings.v4_0.cte_multi_modal_v4_00 import (
    Multimodal,
    MultimodalIndNegociavel,
)
from nfelib.cte.bindings.v4_0.cte_os_v4_00 import CteOs
from nfelib.cte.bindings.v4_0.cte_tipos_basico_v4_00 import (
    CompTpComp,
    Icms00Cst,
    Icms20Cst,
    Icms45Cst,
    Icms60Cst,
    Icms90Cst,
    IcmsoutraUfCst,
    IcmssnCst,
    IcmssnIndSn,
    Tcrt,
    Tcte,
    TcteOs,
    TdocAssoc,
    TendOrg,
    TendReEnt,
    TendeEmi,
    Tendereco,
    Tendernac,
    TfinCte,
    TfinGtve,
    Tgtve,
    Timp,
    TimpOs,
    Tlocal,
    TmodTranspOs,
    TprocEmi,
    TprotCte,
    TprotCteOs,
    TprotGtve,
    TrespTec,
    TretCte,
    TretCteOs,
    TretGtve,
    TunidCarga,
    TunidadeTransp,
    ComDataTpPer,
    ComHoraTpHor,
    IdeIndGlobalizado,
    IdeIndIetoma,
    IdeModal,
    IdeRetira,
    IdeTpEmis,
    IdeTpImp,
    IdeTpServ,
    InfCteSubIndAlteraToma,
    InfEspecieTpEspecie,
    InfEspecieTpNumerario,
    InfOutrosTpDoc,
    InfQCUnid,
    NoInterTpHor,
    NoPeriodoTpPer,
    SegRespSeg,
    SemDataTpPer,
    SemHoraTpHor,
    Toma3Toma,
    Toma4Toma,
    TomaTerceiroToma,
    TomaToma,
)
from nfelib.cte.bindings.v4_0.cte_v4_00 import Cte
from nfelib.cte.bindings.v4_0.ev_canc_cecte_v4_00 import (
    EvCancCecte,
    EvCancCecteDescEvento,
)
from nfelib.cte.bindings.v4_0.ev_canc_cte_v4_00 import (
    EvCancCte,
    EvCancCteDescEvento,
)
from nfelib.cte.bindings.v4_0.ev_canc_iecte_v4_00 import (
    EvCancIecte,
    EvCancIecteDescEvento,
)
from nfelib.cte.bindings.v4_0.ev_canc_prest_desacordo_v4_00 import (
    EvCancPrestDesacordo,
    EvCancPrestDesacordoDescEvento,
)
from nfelib.cte.bindings.v4_0.ev_cce_cte_v4_00 import (
    EvCceCte,
    EvCceCteDescEvento,
    EvCceCteXCondUso,
)
from nfelib.cte.bindings.v4_0.ev_cecte_v4_00 import (
    EvCecte,
    EvCecteDescEvento,
)
from nfelib.cte.bindings.v4_0.ev_epeccte_v4_00 import (
    EvEpeccte,
    EvEpeccteDescEvento,
    EvEpeccteTpCte,
)
from nfelib.cte.bindings.v4_0.ev_gtv_v4_00 import (
    EvGtv,
    EvGtvDescEvento,
)
from nfelib.cte.bindings.v4_0.ev_iecte_v4_00 import (
    EvIecte,
    EvIecteDescEvento,
    EvIecteTpMotivo,
)
from nfelib.cte.bindings.v4_0.ev_prest_desacordo_v4_00 import (
    EvPrestDesacordo,
    EvPrestDesacordoDescEvento,
    EvPrestDesacordoIndDesacordoOper,
)
from nfelib.cte.bindings.v4_0.ev_reg_multimodal_v4_00 import (
    EvRegMultimodal,
    EvRegMultimodalDescEvento,
)
from nfelib.cte.bindings.v4_0.evento_cte_tipos_basico_v4_00 import (
    Tevento,
    TmodTransp,
    TprocEvento,
    TretEvento,
)
from nfelib.cte.bindings.v4_0.evento_cte_v4_00 import EventoCte
from nfelib.cte.bindings.v4_0.gtve_v4_00 import Gtve
from nfelib.cte.bindings.v4_0.inut_cte_tipos_basico_v4_00 import (
    TinutCte,
    TprocInutCte,
    TretInutCte,
)
from nfelib.cte.bindings.v4_0.inut_cte_v4_00 import InutCte
from nfelib.cte.bindings.v4_0.proc_cte_os_v4_00 import CteOsproc
from nfelib.cte.bindings.v4_0.proc_cte_v4_00 import CteProc
from nfelib.cte.bindings.v4_0.proc_evento_cte_v4_00 import ProcEventoCte
from nfelib.cte.bindings.v4_0.proc_gtve_v4_00 import GtveProc
from nfelib.cte.bindings.v4_0.proc_inut_cte_v4_00 import ProcInutCte
from nfelib.cte.bindings.v4_0.ret_cons_sit_cte_v4_00 import RetConsSitCte
from nfelib.cte.bindings.v4_0.ret_cons_stat_serv_cte_v4_00 import RetConsStatServCte
from nfelib.cte.bindings.v4_0.ret_cte_os_v4_00 import RetCteOs
from nfelib.cte.bindings.v4_0.ret_cte_v4_00 import RetCte
from nfelib.cte.bindings.v4_0.ret_evento_cte_v4_00 import RetEventoCte
from nfelib.cte.bindings.v4_0.ret_gtve_v4_00 import RetGtve
from nfelib.cte.bindings.v4_0.ret_inut_cte_v4_00 import RetInutCte
from nfelib.cte.bindings.v4_0.tipos_geral_cte_v4_00 import (
    Tamb,
    TcorgaoIbge,
    TcodUfIbge,
    TmodCt,
    TmodCtos,
    TmodCtCargaOs,
    TmodGtve,
    TmodNf,
    TrsakeyValueType,
    TufSemEx,
    Tuf,
    TtipoUnidCarga,
    TtipoUnidTransp,
)
from nfelib.cte.bindings.v4_0.xmldsig_core_schema_v1_01 import (
    KeyInfoType,
    ReferenceType,
    Signature,
    SignatureType,
    SignatureValueType,
    SignedInfoType,
    TtransformUri,
    TransformType,
    TransformsType,
    X509DataType,
)

__all__ = [
    "TconsSitCte",
    "TretConsSitCte",
    "ProcEventoCteVersao",
    "ProtCteVersao",
    "ConsSitCte",
    "ConsStatServCte",
    "TconsStatServ",
    "TretConsStatServ",
    "Aereo",
    "InfTotApUniAp",
    "NatCargaCInfManu",
    "Aquav",
    "AquavDirec",
    "AquavTpNav",
    "Duto",
    "TenderFer",
    "Ferrov",
    "FerrovTpTraf",
    "TrafMutFerrEmi",
    "TrafMutRespFat",
    "InfFretamentoTpFretamento",
    "PropTpProp",
    "RodoOs",
    "Rodo",
    "Multimodal",
    "MultimodalIndNegociavel",
    "CteOs",
    "CompTpComp",
    "Icms00Cst",
    "Icms20Cst",
    "Icms45Cst",
    "Icms60Cst",
    "Icms90Cst",
    "IcmsoutraUfCst",
    "IcmssnCst",
    "IcmssnIndSn",
    "Tcrt",
    "Tcte",
    "TcteOs",
    "TdocAssoc",
    "TendOrg",
    "TendReEnt",
    "TendeEmi",
    "Tendereco",
    "Tendernac",
    "TfinCte",
    "TfinGtve",
    "Tgtve",
    "Timp",
    "TimpOs",
    "Tlocal",
    "TmodTranspOs",
    "TprocEmi",
    "TprotCte",
    "TprotCteOs",
    "TprotGtve",
    "TrespTec",
    "TretCte",
    "TretCteOs",
    "TretGtve",
    "TunidCarga",
    "TunidadeTransp",
    "ComDataTpPer",
    "ComHoraTpHor",
    "IdeIndGlobalizado",
    "IdeIndIetoma",
    "IdeModal",
    "IdeRetira",
    "IdeTpEmis",
    "IdeTpImp",
    "IdeTpServ",
    "InfCteSubIndAlteraToma",
    "InfEspecieTpEspecie",
    "InfEspecieTpNumerario",
    "InfOutrosTpDoc",
    "InfQCUnid",
    "NoInterTpHor",
    "NoPeriodoTpPer",
    "SegRespSeg",
    "SemDataTpPer",
    "SemHoraTpHor",
    "Toma3Toma",
    "Toma4Toma",
    "TomaTerceiroToma",
    "TomaToma",
    "Cte",
    "EvCancCecte",
    "EvCancCecteDescEvento",
    "EvCancCte",
    "EvCancCteDescEvento",
    "EvCancIecte",
    "EvCancIecteDescEvento",
    "EvCancPrestDesacordo",
    "EvCancPrestDesacordoDescEvento",
    "EvCceCte",
    "EvCceCteDescEvento",
    "EvCceCteXCondUso",
    "EvCecte",
    "EvCecteDescEvento",
    "EvEpeccte",
    "EvEpeccteDescEvento",
    "EvEpeccteTpCte",
    "EvGtv",
    "EvGtvDescEvento",
    "EvIecte",
    "EvIecteDescEvento",
    "EvIecteTpMotivo",
    "EvPrestDesacordo",
    "EvPrestDesacordoDescEvento",
    "EvPrestDesacordoIndDesacordoOper",
    "EvRegMultimodal",
    "EvRegMultimodalDescEvento",
    "Tevento",
    "TmodTransp",
    "TprocEvento",
    "TretEvento",
    "EventoCte",
    "Gtve",
    "TinutCte",
    "TprocInutCte",
    "TretInutCte",
    "InutCte",
    "CteOsproc",
    "CteProc",
    "ProcEventoCte",
    "GtveProc",
    "ProcInutCte",
    "RetConsSitCte",
    "RetConsStatServCte",
    "RetCteOs",
    "RetCte",
    "RetEventoCte",
    "RetGtve",
    "RetInutCte",
    "Tamb",
    "TcorgaoIbge",
    "TcodUfIbge",
    "TmodCt",
    "TmodCtos",
    "TmodCtCargaOs",
    "TmodGtve",
    "TmodNf",
    "TrsakeyValueType",
    "TufSemEx",
    "Tuf",
    "TtipoUnidCarga",
    "TtipoUnidTransp",
    "KeyInfoType",
    "ReferenceType",
    "Signature",
    "SignatureType",
    "SignatureValueType",
    "SignedInfoType",
    "TtransformUri",
    "TransformType",
    "TransformsType",
    "X509DataType",
]
