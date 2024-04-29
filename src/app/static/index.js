function deleteTeam(teamId) {
    fetch(`/delete-team`, {
        method: 'DELETE',
        body: JSON.stringify({ teamId: teamId })
    }).then(response => {
        if (response.ok) {
            window.location.href = '/';
        }
    });
}