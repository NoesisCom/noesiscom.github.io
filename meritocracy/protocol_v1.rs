// meritocracy_protocol_v1.rs
// filtering noise from the architecture

pub fn evaluate_node(node_data: Node) -> LogicStatus {
    if node_data.utility_score < THRESHOLD {
        return LogicStatus::Filtered("noise detected: zero utility");
    }
    
    match node_data.contribution_type {
        Contribution::CipherBreach => integrate_node(node_data, bounty_weight::HIGH),
        Contribution::ArchitecturalBuild => integrate_node(node_data, bounty_weight::MAX),
        Contribution::SocialBegging => purge_node(node_data),
    }
}
